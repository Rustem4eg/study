import csv
import json
from pathlib import Path

# Определение пути к текущему файлу
current_file = Path(__file__).resolve()
BASE_DIR = current_file.parent

# Чтение данных из CSV файла и конвертация в JSON
def csv_to_json(file_path):
    fieldnames = None
    data = []

    with open(file_path, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        fieldnames = reader.fieldnames
        for row in reader:
            data.append({k: v for k, v in row.items()})

    return data

# Путь к CSV файлу
csv_file = BASE_DIR / 'prices.csv'

# Конвертация и вывод JSON
if csv_file.exists():
    data = csv_to_json(csv_file)
    print(json.dumps(data, indent=4))
else:
    print(f"Файл {csv_file} не найден.")