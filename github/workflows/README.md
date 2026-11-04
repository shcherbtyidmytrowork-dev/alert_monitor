# Alert Monitor — збірка APK через GitHub (все в браузері)

## Файли
- `main.py` — інтерфейс Android (Kivy)
- `core.py` — двигун Telegram з вашого alert_monitor_app.py (логіка без змін)
- `buildozer.spec` — налаштування збірки
- `.github/workflows/build.yml` — автоматична збірка APK

## Кроки
1. github.com → **New repository** (назва довільна, можна Private) → Create.
2. У репозиторії: **Add file → Upload files** → завантажте `main.py`, `core.py`, `buildozer.spec` → Commit.
3. **Add file → Create new file**. В полі імені введіть `.github/workflows/build.yml`
   (слеші створять папки), вставте вміст файлу build.yml → Commit.
4. Вкладка **Actions** → «Build APK» (запускається сама після коміту, або Run workflow).
   Перша збірка ~15–30 хв.
5. Відкрийте завершений запуск → внизу **Artifacts → alert-monitor-apk** → завантажте zip → розпакуйте → `.apk`.
6. Скопіюйте APK на телефон, дозвольте встановлення з невідомих джерел, встановіть.

## Перший запуск
1. «Налашт.» → API ID і API Hash (my.telegram.org) → Зберегти.
2. «Запустити» → оберіть вхід: «Код підтвердження» (рекомендовано) або Telegram-посилання.
3. «Налашт.» → «Дозволити роботу у фоні» (вимкнути оптимізацію батареї).
4. Канали та ключові слова — вкладка «Канали»; тригери/повний конфіг — вкладка «JSON».
