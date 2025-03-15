import requests
import colorama
from colorama import Fore, Style
colorama.init(autoreset=True)

API_KEY = "ea7f66782aeed84b1cc00004a51eacfc87dc8fdb"  # Укажите ваш API-ключ DaData

def search_fms_unit(fms_code):
    url = "https://suggestions.dadata.ru/suggestions/api/4_1/rs/suggest/fms_unit"
    headers = {
        "Authorization": f"Token {API_KEY}",
        "Content-Type": "application/json"
    }
    payload = {
        "query": fms_code
    }

    try:
        response = requests.post(url, headers=headers, json=payload)
        if response.status_code == 200:
            data = response.json()
            if data.get('suggestions'):
                print(Fore.LIGHTGREEN_EX + "Результаты поиска подразделения ФМС:" + Style.RESET_ALL)
                for item in data['suggestions']:
                    print(Fore.LIGHTYELLOW_EX + f"Код подразделения: {item['data']['code']}")
                    print(f"Наименование: {item['value']}\n" + Style.RESET_ALL)
            else:
                print(Fore.LIGHTRED_EX + "Подразделение не найдено." + Style.RESET_ALL)
        else:
            print(Fore.LIGHTRED_EX + f"Ошибка: {response.status_code} - {response.text}" + Style.RESET_ALL)
    except Exception as e:
        print(Fore.LIGHTRED_EX + f"Произошла ошибка: {str(e)}" + Style.RESET_ALL)

# Пример использования
fms_code = input(Fore.LIGHTGREEN_EX + "Введите код подразделения ФМС: " + Style.RESET_ALL)
search_fms_unit(fms_code)
