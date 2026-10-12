import json
import os
import re
import time
import urllib.error
import urllib.parse
import urllib.request
from datetime import datetime
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
CONFIG_PATH = BASE_DIR / "config.json"
MEDIA_DIR = BASE_DIR / "saved_media"
MEDIA_DIR.mkdir(exist_ok=True)
CONFIG = {}
API_BASE = ""


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


def api(method, payload=None, timeout=40):
    data = json.dumps(payload or {}).encode("utf-8")
    request = urllib.request.Request(
        f"{API_BASE}/{method}",
        data=data,
        headers={"Content-Type": "application/json"},
    )
    with urllib.request.urlopen(request, timeout=timeout) as response:
        result = json.loads(response.read().decode("utf-8"))
    if not result.get("ok"):
        raise RuntimeError(result.get("description", "Telegram API error"))
    return result["result"]


def download_file(file_path, destination):
    url = f"https://api.telegram.org/file/bot{CONFIG['bot_token']}/{file_path}"
    request = urllib.request.Request(url)
    with urllib.request.urlopen(request, timeout=120) as response, open(destination, "wb") as output:
        while True:
            chunk = response.read(1024 * 256)
            if not chunk:
                break
            output.write(chunk)


def send_message(chat_id, text, reply_to=None):
    payload = {"chat_id": chat_id, "text": text}
    if reply_to is not None:
        payload["reply_to_message_id"] = reply_to
    api("sendMessage", payload)


def media_info(message):
    if message.get("photo"):
        return message["photo"][-1], ".jpg", "photo"
    for key, label, default_ext in (
        ("video", "video", ".mp4"),
        ("animation", "animation", ".mp4"),
        ("document", "document", ".bin"),
        ("audio", "audio", ".mp3"),
        ("voice", "voice", ".ogg"),
        ("video_note", "video-note", ".mp4"),
    ):
        item = message.get(key)
        if item:
            ext = Path(item.get("file_name", "")).suffix
            if not ext or not re.fullmatch(r"\.[A-Za-z0-9]{1,10}", ext):
                ext = default_ext
            return item, ext, label
    return None


def handle_message(message):
    sender = message.get("from") or {}
    chat = message.get("chat") or {}
    chat_id = chat.get("id")
    if sender.get("id") != CONFIG["owner_id"] or chat.get("type") != "private":
        if chat_id is not None and chat.get("type") == "private":
            send_message(chat_id, "Access denied.")
        return

    text = (message.get("text") or "").strip()
    command = text.split(maxsplit=1)[0].split("@", 1)[0] if text else ""

    if command == "/start":
        send_message(chat_id, "Media Saver is ready.\n\nSend a photo, video, animation, document, audio, voice message, or video note here. The file will be saved on this device.\n\n/status — storage status\n/help — help", message.get("message_id"))
        return
    if command == "/help":
        send_message(chat_id, "Send media directly to this bot to save it in saved_media/.\nSupported: photos, videos, animations, documents, audio, voice messages, and video notes.\n/status — number and total size of saved files", message.get("message_id"))
        return
    if command == "/status":
        files = [p for p in MEDIA_DIR.iterdir() if p.is_file()]
        total = sum(p.stat().st_size for p in files)
        send_message(chat_id, f"Saved files: {len(files)}\nTotal size: {total / (1024 * 1024):.2f} MB", message.get("message_id"))
        return

    info = media_info(message)
    if not info:
        return

    item, ext, label = info
    stamp = datetime.now().strftime("%Y%m%d_%H%M%S_%f")
    file_id = re.sub(r"[^A-Za-z0-9_-]", "", item.get("file_id", ""))[:24]
    destination = MEDIA_DIR / f"{stamp}_{label}_{file_id}{ext}"

    try:
        file_data = api("getFile", {"file_id": item["file_id"]})
        download_file(file_data["file_path"], destination)
        size_mb = destination.stat().st_size / (1024 * 1024)
        send_message(chat_id, f"Saved: {destination.name}\nSize: {size_mb:.2f} MB", message.get("message_id"))
    except Exception as exc:
        destination.unlink(missing_ok=True)
        print(f"Media download failed: {type(exc).__name__}: {exc}")
        send_message(chat_id, f"Download failed: {type(exc).__name__}", message.get("message_id"))


def main():
    global CONFIG, API_BASE
    CONFIG = load_config()
    API_BASE = f"https://api.telegram.org/bot{CONFIG['bot_token']}"
    me = api("getMe")
    print(f"Running as @{me.get('username') or me['id']}. Press Ctrl+C to stop.")
    offset = 0
    while True:
        try:
            updates = api("getUpdates", {"offset": offset, "timeout": 30, "allowed_updates": ["message"]}, timeout=40)
            for update in updates:
                offset = update["update_id"] + 1
                message = update.get("message")
                if message:
                    try:
                        handle_message(message)
                    except Exception as exc:
                        print(f"Message handling failed: {type(exc).__name__}: {exc}")
        except KeyboardInterrupt:
            raise
        except Exception as exc:
            print(f"Connection error: {type(exc).__name__}: {exc}")
            time.sleep(3)


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nStopped.")
