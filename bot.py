import asyncio
import json
import os
import re
from datetime import datetime
from pathlib import Path

from aiogram import Bot, Dispatcher, F
from aiogram.filters import Command
from aiogram.types import Message

BASE_DIR = Path(__file__).resolve().parent
CONFIG_PATH = BASE_DIR / "config.json"
MEDIA_DIR = BASE_DIR / "saved_media"
MEDIA_DIR.mkdir(exist_ok=True)
dp = Dispatcher()


def load_config():
    if CONFIG_PATH.exists():
        try:
            data = json.loads(CONFIG_PATH.read_text(encoding="utf-8"))
            if data.get("bot_token") and str(data.get("owner_id", "")).isdigit():
                return data
        except (json.JSONDecodeError, OSError):
            pass

    print("\nTelegram Media Saver — first-time setup\n")
    token = input("BotFather token: ").strip()
    if not token:
        raise SystemExit("Token cannot be empty.")
    owner_text = input("Numeric Telegram owner ID: ").strip()
    if not owner_text.isdigit():
        raise SystemExit("Owner ID must contain digits only.")

    data = {"bot_token": token, "owner_id": int(owner_text)}
    CONFIG_PATH.write_text(json.dumps(data, indent=2), encoding="utf-8")
    try:
        os.chmod(CONFIG_PATH, 0o600)
    except OSError:
        pass
    print("Configuration saved. It will not be requested again.\n")
    return data


def is_owner(message: Message, owner_id: int) -> bool:
    return bool(message.from_user and message.from_user.id == owner_id)


def media_info(message: Message):
    if message.photo:
        item = message.photo[-1]
        return item, ".jpg", "photo"
    for attr, label, default_ext in (
        ("video", "video", ".mp4"),
        ("animation", "animation", ".mp4"),
        ("document", "document", ".bin"),
        ("audio", "audio", ".mp3"),
        ("voice", "voice", ".ogg"),
        ("video_note", "video note", ".mp4"),
    ):
        item = getattr(message, attr, None)
        if item:
            ext = Path(getattr(item, "file_name", "") or "").suffix
            if not ext or not re.fullmatch(r"\.[A-Za-z0-9]{1,10}", ext):
                ext = default_ext
            return item, ext, label
    return None


@dp.message(Command("start"))
async def start(message: Message, bot: Bot):
    config = bot["config"]
    if not is_owner(message, config["owner_id"]):
        await message.answer("Access denied.")
        return
    await message.answer(
        "Media Saver is ready.\n\n"
        "Send a photo, video, animation, document, audio, voice message, or video note here. "
        "The file will be saved on this device.\n\n"
        "/status — storage status\n/help — help"
    )


@dp.message(Command("help"))
async def help_command(message: Message, bot: Bot):
    if not is_owner(message, bot["config"]["owner_id"]):
        await message.answer("Access denied.")
        return
    await message.answer(
        "Send media directly to this bot to save it in saved_media/.\n"
        "Supported: photos, videos, animations, documents, audio, voice messages, and video notes.\n"
        "/status — number and total size of saved files"
    )


@dp.message(Command("status"))
async def status(message: Message, bot: Bot):
    if not is_owner(message, bot["config"]["owner_id"]):
        await message.answer("Access denied.")
        return
    files = [p for p in MEDIA_DIR.iterdir() if p.is_file()]
    total = sum(p.stat().st_size for p in files)
    await message.answer(f"Saved files: {len(files)}\nTotal size: {total / (1024 * 1024):.2f} MB")


@dp.message(F.photo | F.video | F.animation | F.document | F.audio | F.voice | F.video_note)
async def save_media(message: Message, bot: Bot):
    config = bot["config"]
    if not is_owner(message, config["owner_id"]):
        await message.answer("Access denied.")
        return

    info = media_info(message)
    if not info:
        await message.answer("Unsupported media.")
        return

    item, ext, label = info
    stamp = datetime.now().strftime("%Y%m%d_%H%M%S_%f")
    file_id = re.sub(r"[^A-Za-z0-9_-]", "", item.file_id)[:24]
    destination = MEDIA_DIR / f"{stamp}_{label.replace(' ', '-')}_{file_id}{ext}"

    try:
        telegram_file = await bot.get_file(item.file_id)
        await bot.download_file(telegram_file.file_path, destination=destination)
        size_mb = destination.stat().st_size / (1024 * 1024)
        await message.answer(f"Saved: {destination.name}\nSize: {size_mb:.2f} MB")
    except Exception as exc:
        destination.unlink(missing_ok=True)
        await message.answer(f"Download failed: {type(exc).__name__}")


async def main():
    config = load_config()
    bot = Bot(token=config["bot_token"])
    bot["config"] = config
    try:
        me = await bot.get_me()
        print(f"Running as @{me.username or me.id}. Press Ctrl+C to stop.")
        await dp.start_polling(bot)
    finally:
        await bot.session.close()


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("\nStopped.")
