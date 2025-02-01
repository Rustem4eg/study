import csv
from pathlib import Path


# Определение функций
def write_to_csv(file_path, data):
    with open(file_path, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=['Дата', 'Продукт', 'Сумма'])
        writer.writeheader()
        writer.writerows(data)

# Данные для записи в CSV файл
data = [
    {'Дата': '2023-01-01', 'Продукт': 'Продукт A', 'Сумма': '500'},
    {'Дата': '2023-02-15', 'Продукт': 'Продукт B', 'Сумма': '700'},
    {'Дата': '2023-03-10', 'Продукт': 'Продукт A', 'Сумма': '800'},
    {'Дата': '2023-04-05', 'Продукт': 'Продукт C', 'Сумма': '600'},
    {'Дата': '2023-04-20', 'Продукт': 'Продукт B', 'Сумма': '900'},
    {'Дата': '2023-05-12', 'Продукт': 'Продукт A', 'Сумма': '1000'}
]

# Путь к файлу
BASE_DIR = Path(__file__).resolve().parent
csv_file = BASE_DIR / 'task2.csv'

# Запись данных в CSV файл
write_to_csv(csv_file, data)

# Функция для чтения данных из CSV файла
def read_csv_file(file_path):
    with open(file_path, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        return list(reader)

# Функция для подсчета общей суммы продаж
def calculate_total_sales(sales_data):
    total_sales = 0
    for sale in sales_data:
        total_sales += float(sale['Сумма'])
    return total_sales

# Функция для поиска продукта с самым высоким объемом продаж
def find_highest_sales_product(sales_data):
    highest_sales_product = None
    highest_sales = 0
    for product in set(sale['Продукт'] for sale in sales_data):
        product_sales = sum(float(sale['Сумма']) for sale in sales_data if sale['Продукт'] == product)
        if product_sales > highest_sales:
            highest_sales = product_sales
            highest_sales_product = product
    return highest_sales_product

# Функция для группировки данных по месяцам и подсчета общей суммы продаж
def group_sales_by_month(sales_data):
    sales_by_month = {}
    for sale in sales_data:
        month = sale['Дата'].split('-')[1]
        if month not in sales_by_month:
            sales_by_month[month] = 0
        sales_by_month[month] += float(sale['Сумма'])
    return sales_by_month

# Чтение данных из CSV файла
sales_data = read_csv_file(csv_file)

# Подсчет общей суммы продаж
total_sales = calculate_total_sales(sales_data)
print(f"Общая сумма продаж: {total_sales}")

# Поиск продукта с самым высоким объемом продаж
highest_sales_product = find_highest_sales_product(sales_data)
print(f"Продукт с самым высоким объемом продаж: {highest_sales_product}")

# Группировка данных по месяцам и вывод общей суммы продаж для каждого месяца
sales_by_month = group_sales_by_month(sales_data)
for month, total_sales in sales_by_month.items():
    print(f"Сумма продаж за месяц {month}: {total_sales}")