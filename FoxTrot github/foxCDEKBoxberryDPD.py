import requests
import colorama
from colorama import Fore, Style
colorama.init(autoreset=True)

API_KEY = "ea7f66782aeed84b1cc00004a51eacfc87dc8fdb"  # Укажите ваш API-ключ DaData

def search_city_with_dadata(city_name):
    url = "https://suggestions.dadata.ru/suggestions/api/4_1/rs/suggest/address"
    headers = {
        "Authorization": f"Token {API_KEY}",
        "Content-Type": "application/json"
    }
    payload = {
        "query": city_name,
        "locations": [{"country": "Россия"}]  # Ограничиваем поиск по России (можно изменить)
    }

    try:
        response = requests.post(url, headers=headers, json=payload)
        if response.status_code == 200:
            data = response.json()
            if data.get('suggestions'):
                print(Fore.LIGHTGREEN_EX + "Результаты поиска города:" + Style.RESET_ALL)
                for item in data['suggestions']:
                    print(Fore.LIGHTYELLOW_EX + f"Город: {item['value']}")
                    print(f"Код ФИАС: {item['data']['fias_id']}")
                    print(f"Код КЛАДР: {item['data']['kladr_id']}\n" + Style.RESET_ALL)
            else:
                print(Fore.LIGHTRED_EX + "Город не найден." + Style.RESET_ALL)
        else:
            print(Fore.LIGHTRED_EX + f"Ошибка: {response.status_code} - {response.text}" + Style.RESET_ALL)
    except Exception as e:
        print(Fore.LIGHTRED_EX + f"Произошла ошибка: {str(e)}" + Style.RESET_ALL)

# Пример использования
city_name = input(Fore.LIGHTGREEN_EX + "Введите название города: " + Style.RESET_ALL)
search_city_with_dadata(city_name)
