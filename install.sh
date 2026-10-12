#!/data/data/com.termux/files/usr/bin/bash
set -e
cd "$(dirname "$0")"
pkg update -y
pkg install -y python
python -m py_compile bot.py
mkdir -p saved_media
chmod 700 .
chmod 700 saved_media
echo
echo "Installation complete. Run ./start.sh"
