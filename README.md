<div align="center">

<img src="https://capsule-render.vercel.app/api?type=waving&color=0:050505,35:171717,70:303030,100:050505&height=190&section=header&text=Telegram%20Media%20Saver&fontSize=54&fontColor=ffffff&fontAlignY=38&desc=SAVE%20MEDIA%20INTO%20TERMUX%20STORAGE&descAlignY=62&descSize=13" width="100%" />

<br/>

<img src="https://img.shields.io/badge/PYTHON-111111?style=for-the-badge&logo=python&logoColor=white" /> <img src="https://img.shields.io/badge/TERMUX-111111?style=for-the-badge&logo=termux&logoColor=white" /> <img src="https://img.shields.io/badge/TELEGRAM-111111?style=for-the-badge&logo=telegram&logoColor=white" /> <img src="https://img.shields.io/github/stars/TheROMZ52/telegram-media-saver-termux?style=for-the-badge&color=111111&labelColor=050505&logo=github" /> <img src="https://img.shields.io/github/last-commit/TheROMZ52/telegram-media-saver-termux?style=for-the-badge&color=111111&labelColor=050505" />

<br/>

## Telegram Media Saver for Termux

[English](README.md) · [فارسی](README.fa.md)

### A tiny Termux helper that saves the media you send it. Finally, your Downloads folder has a plan.

<img src="https://skillicons.dev/icons?i=py,bash,linux&theme=dark" />

</div>

---

A personal Telegram bot that saves media sent directly to the bot into a local folder on an Android device running Termux.

---

## 01 / REQUIREMENTS

- Android with Termux
- A Telegram bot token from [@BotFather](https://t.me/BotFather)
- Your numeric Telegram user ID

---

## 02 / INSTALL

Clone the repository, then run:

```bash
bash install.sh
```

---

## 03 / START

```bash
bash start.sh
```

On first launch, the script asks for the bot token and numeric owner ID. The settings are stored locally in `config.json`; later launches reuse them.

Keep `config.json` private. Do not commit or share it.

---

## 04 / USE

Open your bot in Telegram and send `/start`. Send a photo, video, animation, document, audio file, voice message, or video note directly to the bot. Files are stored in `saved_media/`.

- `/status` — number and total size of saved files
- `/help` — usage information

Stop the bot with Ctrl+C in Termux.

---

## 05 / IMPORTANT LIMITS

This bot can only save media that Telegram delivers to it. It cannot retrieve view-once media from another private chat or bypass Telegram's restrictions. Telegram Bot API file-download limits apply; very large files may fail.

The bot is owner-restricted by Telegram numeric user ID. Do not share the bot token.

---

<div align="center">

<a href="https://github.com/TheROMZ52?tab=repositories"><img src="https://img.shields.io/badge/MORE%20PROJECTS-111111?style=for-the-badge&logo=github&logoColor=white" /></a>

<br/><br/>

<img src="https://capsule-render.vercel.app/api?type=waving&color=0:050505,50:202020,100:050505&height=110&section=footer" width="100%" />

<sub>© TheROMZ52 • Built with code, curiosity, and a suspicious number of tabs.</sub>

</div>
