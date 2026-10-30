[English](README.md) · [فارسی](README.fa.md)

# Telegram Media Saver for Termux

A tiny Termux helper that saves the media you send it. Finally, your Downloads folder has a plan.

A personal Telegram bot that saves media sent directly to the bot into a local folder on an Android device running Termux.

## Requirements

- Android with Termux
- A Telegram bot token from [@BotFather](https://t.me/BotFather)
- Your numeric Telegram user ID

## Install

Clone the repository, then run:

```bash
bash install.sh
```

## Start

```bash
bash start.sh
```

On first launch, the script asks for the bot token and numeric owner ID. The settings are stored locally in `config.json`; later launches reuse them.

Keep `config.json` private. Do not commit or share it.

## Use

Open your bot in Telegram and send `/start`. Send a photo, video, animation, document, audio file, voice message, or video note directly to the bot. Files are stored in `saved_media/`.

- `/status` — number and total size of saved files
- `/help` — usage information

Stop the bot with Ctrl+C in Termux.

## Important limits

This bot can only save media that Telegram delivers to it. It cannot retrieve view-once media from another private chat or bypass Telegram's restrictions. Telegram Bot API file-download limits apply; very large files may fail.

The bot is owner-restricted by Telegram numeric user ID. Do not share the bot token.
