<div align="center">

<img src="https://capsule-render.vercel.app/api?type=waving&color=0:050505,35:171717,70:303030,100:050505&height=190&section=header&text=Telegram%20Media%20Saver&fontSize=54&fontColor=ffffff&fontAlignY=38&desc=SAVE%20MEDIA%20INTO%20TERMUX%20STORAGE&descAlignY=62&descSize=13" width="100%" />

<br/>

<img src="https://img.shields.io/badge/PYTHON-111111?style=for-the-badge&logo=python&logoColor=white" /> <img src="https://img.shields.io/badge/TERMUX-111111?style=for-the-badge&logo=termux&logoColor=white" /> <img src="https://img.shields.io/badge/TELEGRAM-111111?style=for-the-badge&logo=telegram&logoColor=white" /> <img src="https://img.shields.io/github/stars/TheROMZ52/telegram-media-saver-termux?style=for-the-badge&color=111111&labelColor=050505&logo=github" /> <img src="https://img.shields.io/github/last-commit/TheROMZ52/telegram-media-saver-termux?style=for-the-badge&color=111111&labelColor=050505" />

<br/>

## ذخیره‌کنندهٔ رسانهٔ تلگرام برای Termux

### یه ابزار کوچیک Termux برای ذخیره‌ی رسانه‌هایی که براش می‌فرستی؛ بالاخره پوشه‌ی دانلودها یه برنامه‌ای پیدا کرد.

<img src="https://skillicons.dev/icons?i=py,bash,linux&theme=dark" />

</div>

---

یک ربات شخصی تلگرام که رسانه‌هایی را که مستقیماً برای ربات ارسال می‌کنی، در پوشه‌ای محلی روی دستگاه اندرویدی مجهز به Termux ذخیره می‌کند.

---

## 01 / پیش‌نیازها

- دستگاه اندرویدی با Termux
- توکن ربات تلگرام از [@BotFather](https://t.me/BotFather)
- شناسهٔ عددی حساب تلگرام خودت

---

## 02 / نصب

مخزن را Clone کن و دستور زیر را اجرا کن:

```bash
bash install.sh
```

---

## 03 / اجرا

```bash
bash start.sh
```

در اولین اجرا، اسکریپت توکن ربات و شناسهٔ عددی مالک را می‌پرسد. تنظیمات به‌صورت محلی در `config.json` ذخیره می‌شوند و در اجراهای بعدی دوباره استفاده خواهند شد.

**فایل `config.json` را خصوصی نگه دار و آن را Commit یا برای دیگران ارسال نکن.**

---

## 04 / استفاده

ربات را در تلگرام باز کن و دستور `/start` را بفرست. سپس یک عکس، ویدئو، انیمیشن، سند، فایل صوتی، پیام صوتی یا ویدئوی گرد را مستقیماً برای ربات ارسال کن.

فایل‌ها در پوشهٔ `saved_media/` ذخیره می‌شوند.

- `/status` — تعداد و حجم کل فایل‌های ذخیره‌شده
- `/help` — راهنمای استفاده

برای توقف ربات، در Termux کلیدهای Ctrl+C را بزن.

---

## 05 / محدودیت‌های مهم

این ربات فقط رسانه‌هایی را ذخیره می‌کند که تلگرام به خود ربات تحویل می‌دهد. نمی‌تواند رسانه‌های یک‌بارمصرف را از گفتگوی خصوصی دیگران بازیابی کند یا محدودیت‌های تلگرام را دور بزند.

محدودیت‌های دانلود فایل در Telegram Bot API همچنان اعمال می‌شوند؛ بنابراین ممکن است دانلود فایل‌های بسیار بزرگ با خطا مواجه شود.

دسترسی ربات با شناسهٔ عددی تلگرام مالک محدود شده است. توکن ربات را در اختیار دیگران قرار نده.

---

<div align="center">

<a href="https://github.com/TheROMZ52?tab=repositories"><img src="https://img.shields.io/badge/MORE%20PROJECTS-111111?style=for-the-badge&logo=github&logoColor=white" /></a>

<br/><br/>

<img src="https://capsule-render.vercel.app/api?type=waving&color=0:050505,50:202020,100:050505&height=110&section=footer" width="100%" />

<sub>© TheROMZ52 • ساخته‌شده با کد، کنجکاوی و تعداد مشکوکی تب باز.</sub>

</div>
