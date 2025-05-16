
📦 Telega.in Checker

Просто и быстро проверяет, существует ли карточка Telega.in по прямому URL.

✅ Что делает:
- Читает список каналов из channels.txt
- Формирует ссылку https://telega.in/channels/<username>/card
- Проверяет, доступна ли она (status 200)
- Сохраняет результат в telega_results_direct.xlsx

🚀 Как запустить:
1. pip install -r requirements.txt
2. Добавь свои каналы в channels.txt (по одной строке)
3. Запусти: python telega_direct_check.py
