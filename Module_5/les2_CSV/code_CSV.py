import csv
# Задание 1:
with open ('prices.txt', 'r', encoding='utf-8') as file:
    reader = csv.reader(file, delimiter='\t')          # Создаем объект reader для чтения данных
    
    
    with open('prices.csv', 'w', newline='', encoding='utf-8') as newfile:  # Создаем новый CSV файл для записи
        writer = csv.writer(newfile)  # Создаем объект writer для записи данных в новый CSV файл
        writer.writerow(['Product Name', 'Quantity', 'Price'])  # Создаем объект writer для записи данных в новый CSV файл
        for row in reader:
            writer.writerow(row)            # Записываем данные из каждой строки


# Задание 2:
with open ('prices.csv', 'r', encoding='utf-8') as csvfile: # Открываем CSV файл
    reader = csv.DictReader(csvfile) # Чтение данных из CSV файла с использованием словаря
    for row in reader:
        total_price = int(row['Quantity'])*int(row['Price'])
        print(f'Стоимость товара {row['Product Name']} в количестве {row['Quantity']} равна {total_price} рублей') # Записываем данные из каждой строки