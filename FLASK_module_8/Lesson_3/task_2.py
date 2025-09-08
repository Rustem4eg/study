import requests
from datetime import datetime

def get_currency_rates():
    """Достаем свежие курсы валют от ЦБ и показываем их"""
    
    # Тот самый адрес, откуда берем данные о валютах
    url = "https://www.cbr-xml-daily.ru/daily_json.js"
    
    try:
        # Пытаемся достучаться до сервера ЦБ
        response = requests.get(url)
        
        # Если сервер ответил "все ок"
        if response.status_code == 200:
            # Разбираем полученные данные (они в формате JSON)
            data = response.json()
            
            # Достаем дату обновления курсов и приводим к красивому виду
            date = data['Date']
            timestamp = datetime.fromisoformat(date.replace('Z', '+00:00'))
            formatted_date = timestamp.strftime("%d.%m.%Y %H:%M")
            
            print(f"📊 Актуальные курсы валют от ЦБ РФ на {formatted_date}")
            print("=" * 50)
            
            # Список валют, которые нам интереснее всего
            main_currencies = ['USD', 'EUR', 'CNY', 'JPY', 'GBP']
            
            # Показываем информацию по каждой валюте из нашего списка
            for currency_code in main_currencies:
                if currency_code in data['Valute']:
                    currency = data['Valute'][currency_code]
                    print(f"{currency['CharCode']} ({currency['Name']}):")
                    print(f"  Стоит: {currency['Value']} рублей")
                    # Считаем разницу с предыдущим значением
                    change = currency['Previous'] - currency['Value']
                    print(f"  Изменился на: {change:+.4f} руб.")
                    print()
            
            # Покажем какие еще валюты есть в данных
            print("💡 Еще доступны курсы по валютам:")
            other_currencies = [code for code in data['Valute'].keys() if code not in main_currencies]
            print(", ".join(other_currencies[:10]) + "...")
            
        else:
            print(f"❌ Что-то пошло не так. Код ошибки: {response.status_code}")
            
    except requests.exceptions.RequestException as e:
        print(f"❌ Не удалось подключиться к серверу: {e}")
    except KeyError as e:
        print(f"❌ В данных что-то не так: {e}")

def save_rates_to_file():
    """Сохраняем курсы в текстовый файл чтобы посмотреть позже"""
    
    url = "https://www.cbr-xml-daily.ru/daily_json.js"
    
    try:
        # Снова запрашиваем данные
        response = requests.get(url)
        
        if response.status_code == 200:
            data = response.json()
            
            # Создаем файл с именем типа "currency_rates_20250909_1430.txt"
            filename = f"currency_rates_{datetime.now().strftime('%Y%m%d_%H%M')}.txt"
            
            # Открываем файл и записываем туда все что нашли
            with open(filename, 'w', encoding='utf-8') as file:
                file.write(f"Курсы валют от Центробанка\n")
                file.write(f"Обновлено: {data['Date']}\n")
                file.write("=" * 50 + "\n\n")
                
                # Перебираем все валюты которые пришли
                for currency_code, currency_data in data['Valute'].items():
                    file.write(f"{currency_code} - {currency_data['Name']}:\n")
                    file.write(f"  Курс: {currency_data['Value']} руб.\n")
                    file.write(f"  За сколько: {currency_data['Nominal']} единиц\n")
                    file.write("-" * 30 + "\n")
            
            print(f"✅ Все записалось в файл: {filename}")
            
    except Exception as e:
        print(f"❌ Не получилось сохранить в файл: {e}")

# Начинаем работу программы здесь
if __name__ == "__main__":
    print("Запрашиваем у ЦБ актуальные курсы валют...")
    get_currency_rates()
    
    # Спросим пользователя хочет ли он сохранить данные
    save_option = input("\nСохранить эти данные в файл? (да/нет): ")
    if save_option.lower() in ['да', 'д', 'y', 'yes']:
        save_rates_to_file()
    else:
        print("Как знаешь! Данные не сохранялись.")