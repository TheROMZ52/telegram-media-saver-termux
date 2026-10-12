#!/data/data/com.termux/files/usr/bin/bash
set -e
cd "$(dirname "$0")"
if ! python -c "import aiogram" >/dev/null 2>&1; then
  echo "Dependencies missing. Run: bash install.sh"
  exit 1
fi
python bot.py
