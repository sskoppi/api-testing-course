import json
import os

# Папка с файлами — та, где лежит этот скрипт
FOLDER = os.path.dirname(os.path.abspath(__file__))

# Файлы, которые надо починить (кроме Заказчики.json — он уже массив)
FILES = {
    "Материалы.json": "Materials",
    "Заказы.json": "Orders",
    "Позиции_заказов.json": "Order_items",
    "Спецификация.json": "Specification",
    "Цены.json": "Prices",
    "Скидки.json": "Sales",
    "Товары.json": "Products",
}

for filename, table_name in FILES.items():
    path = os.path.join(FOLDER, filename)
    if not os.path.exists(path):
        print(f"[SKIP] {filename} не найден")
        continue

    # Читаем JSON
    with open(path, "r", encoding="utf-8") as f:
        data = json.load(f)

    # Если это объект с "records" — достаём массив
    if isinstance(data, dict) and "records" in data:
        records = data["records"]
        print(f"[OK] {filename}: объект -> массив из {len(records)} записей")
    elif isinstance(data, list):
        records = data
        print(f"[OK] {filename}: уже массив из {len(records)} записей")
    else:
        print(f"[??] {filename}: неизвестная структура, пропуск")
        continue

    # Перезаписываем файл чистым массивом
    with open(path, "w", encoding="utf-8") as f:
        json.dump(records, f, ensure_ascii=False, indent=2)

print("\nГотово. Теперь снова конвертируй каждый JSON в CSV.")