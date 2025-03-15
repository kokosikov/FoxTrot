import requests
import os
import colorama
from colorama import Fore, Style

colorama.init(autoreset=True)

API_KEY = 'ea7f66782aeed84b1cc00004a51eacfc87dc8fdb'  # Вставьте свой API-ключ DaData

# Функция для отображения баннера с лисой
def display_banner():
    print(Fore.BLUE + """ 
⠀⠀⠀⠀⢸⠓⢄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⢸⠀⠀⠑⢤⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⢸⡆⠀⠀⠀⠙⢤⡷⠤⠖⠚⡿⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀
⣠⡿⠢⢄⡀⠀⡇⠀⠀⠀⠀⠀⠉⠀⠀⠸⠷⣶⠂⠀⠀⠀⣀⣀⠀⠀⠀
⢸⣃⠀⠀⠉⠳⣷⠞⠁⠀⠀⠀⠀⠀⠀⠀⠈⠉⠉⠉⠉⠉⠉⠉⢉⡭⠋
⠀⠘⣆⠀⠀⠀⠁⠀⢀⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡴⠋⠀⠀
⠀⠀⠘⣦⠆⠀⠀⢀⡎⢹⡀⠀⠀⠀⠀⠀⡀⠀⠀⡀⣠⠔⠋⠀⠀⠀⠀
⠀⠀⠀⡏⠀⠀⣆⠘⣄⠸⢧⠀⢀⣠⠖⢻⠀⠀⠀⣿⢥⣄⣀⣀⣀⠀
⠀⠀⢸⠁⠀⠀⡏⢣⣌⠙⠚⠀⡛⠀⣠⠏⠀⠀⠀⠇⠀⠀⠀⠀⢙⣣⠄
⠀⠀⢸⡀⠀⠀⠳⡞⠈⢻⠶⠤⣉⣉⣡⡔⠀⠀⢀⠀⠀⣀⡤⠖⠚
⠀⠀⡼⣇⠀⠀⠀⠙⠦⣞⡀⠀⢸⣣⠞⠀⠀⠀⡼⠚⠋⠁⠀⠀⠀⠀
⠀⢰⡇⠙⠀⠀⠀⠀⠀⠀⠉⠙⠉⠀⠀⠀⠀⡼⠁⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⢧⡀⠀⢠⡀⠀⠀⠀⠀⠀⠀⠀⠀⠙⣞⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠙⣶⣶⣿⠢⣄⡀⠀⠀⠀⠀⠀⠀⢸⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠉⠀⠀⠀⠙⢿⣳⠀⠀⠀⢀⡞⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠀⣀⡤⠋⠀⠀⠀⠀⠀⠀
                                                            
 @@@@@@   @@@@@@@@   @@@@@@   @@@@@@@    @@@@@@@  @@@  @@@  
@@@@@@@   @@@@@@@@  @@@@@@@@  @@@@@@@@  @@@@@@@@  @@@  @@@  
!@@       @@!       @@!  @@@  @@!  @@@  !@@       @@!  @@@  
!@!       !@!       !@!  @!@  !@!  @!@  !@!       !@!  @!@  
!!@@!!    @!!!:!    @!@!@!@!  @!@!!@!   !@!       @!@!@!@!  
 !!@!!!   !!!!!:    !!!@!!!!  !!@!@!    !!!       !!!@!!!!  
     !:!  !!:       !!:  !!!  !!: :!!   :!!       !!:  !!!  
    !:!   :!:       :!:  !:!  :!:  !:!  :!:       :!:  !:!  
:::: ::    :: ::::  ::   :::  ::   :::   ::: :::  ::   :::  
:: : :    : :: ::    :   : :   :   : :   :: :: :   :   : :   
                                       
    """ + Style.RESET_ALL)

# Функция для поиска по ФИО через DaData
def search_fio_with_dadata(fio):
    url = "https://suggestions.dadata.ru/suggestions/api/4_1/rs/suggest/party"

    headers = {
        "Authorization": f"Token {API_KEY}",
        "Content-Type": "application/json"
    }

    payload = {"query": fio}

    try:
        response = requests.post(url, headers=headers, json=payload)
        if response.status_code == 200:
            data = response.json()
            if data.get('suggestions'):
                print(Fore.LIGHTGREEN_EX + "Результаты поиска:" + Style.RESET_ALL)
                for item in data['suggestions']:
                    print(Fore.LIGHTYELLOW_EX + f"Название: {item['value']}")
                    print(f"ИНН: {item['data']['inn']}")
                    print(f"Адрес: {item['data']['address']['value']}\n" + Style.RESET_ALL)
            else:
                print(Fore.LIGHTRED_EX + "Данные не найдены." + Style.RESET_ALL)
        else:
            print(Fore.LIGHTRED_EX + f"Ошибка: {response.status_code} - {response.text}" + Style.RESET_ALL)
    except Exception as e:
        print(Fore.LIGHTRED_EX + f"Произошла ошибка: {str(e)}" + Style.RESET_ALL)

# Главное меню
def main_menu():
    display_banner()
    while True:
        print("\n--- Главное меню ---")
        print(Fore.RED + "1. Искать по ИНН,Адресу,Кампании,Городу через DaData" + Style.RESET_ALL)
        print(Fore.RED + "2. Искать идентификатор города в СДЭК, Boxberry и DPD" + Style.RESET_ALL)
        print(Fore.RED + "3. Узнать кем выдан паспорт" + Style.RESET_ALL)
        print(Fore.RED + "4. Проверка по реестру МВД " + Style.RESET_ALL)
        print(Fore.RED + "5. Поиск по таможне " + Style.RESET_ALL)
        print(Fore.RED + "6. Выход" + Style.RESET_ALL)

        choice = input(Fore.WHITE + "Выберите опцию (1-6): " + Style.RESET_ALL)

        if choice == "1":
            fio = input(Fore.LIGHTGREEN_EX + "Введите Данные для поиска: " + Style.RESET_ALL)
            search_fio_with_dadata(fio)
        elif choice == "2":
            os.system("python foxCDEKBoxberryDPD.py")
        elif choice == "3":
            os.system("python foxpass.py")
        elif choice == "4":
            os.system("python foxcheckpass.py")
        elif choice == "5":
            os.system("python foxtamojnya.py")
        elif choice == "6":
            print(Fore.LIGHTGREEN_EX + "Выход из программы. До свидания!" + Style.RESET_ALL)
            break
        else:
            print(Fore.LIGHTRED_EX + "Неправильный выбор. Попробуйте снова." + Style.RESET_ALL)

# Запуск программы
main_menu()
