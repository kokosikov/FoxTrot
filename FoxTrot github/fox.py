import requests
import termcolor
import colorama
import os
import re
from colorama import Fore, Style
import phonenumbers
from phonenumbers import geocoder, carrier, timezone

colorama.init(autoreset=True)

API_KEY = '5B06EF3F557D4D793747DB37A7FB8F58'

def display_banner():
    print(Fore.LIGHTYELLOW_EX + """ 
    ⠀⠀⠀⠀⣿⠙⣦⠀⠀⠀⠀⠀⠀⣀⣤⡶⠛⠁ 
    ⠀⠀⠀⠀⢻⠀⠈⠳⠀⠀⣀⣴⡾⠛⠁⣠⠂⢠⠇ 
    ⠀⠀⠀⠀⠈⢀⣀⠤⢤⡶⠟⠁⢀⣴⣟⠀⠀⣾ 
    ⠀⠀⠀⠠⠞⠉⢀⠀⠉⠀⢀⣠⣾⣿⣏⠀⢠⡇ 
    ⠀⠀⡰⠋⠀⢰⠃⠀⠀⠉⠛⠿⠿⠏⠁⠀⣸⠁ 
    ⠀⠀⣄⠀⠀⠏⣤⣤⣀⡀⠀⠀⠀⠀⠀⠾⢯⣀ 
    ⠀⠀⣻⠃⠀⣰⡿⠛⠁⠀⠀⠀⢤⣀⡀⠀⠺⣿⡟⠛⠁ 
    ⢀⡠⠋⡤⠠⠋⠀⠀⢀⠐⠁⠀⠈⣙⢯⡃⠀⢈⡻⣦ 
    ⢰⣷⠇⠀⠀⠀⢀⡠⠃⠀⠀⠀⠀⠈⠻⢯⡄⠀⢻⣿⣷ 
    ⠉⠲⣶⣶⢾⣉⣐⡚⠋⠀⠀⠀⠀⠀⠘⠀⠀⡎⣿⣿⡇ 
    ⠀⠀⠀⠀⣸⣿⣿⣿⣷⡄⠀⠀⢠⣿⣴⠀⠀⣿⣿⣿⣧ 
    ⠀⠀⠀⢀⣴⣿⣿⣿⣿⣿⠇⠀⢠⠟⣿⠏⢀⣾⠟⢸⣿⡇ 
    ⠀⢠⣿⣿⣿⣿⠟⠘⠁⢠⠜⢉⣐⡥⠞⠋⢀⣴⣿⣿⠃ 
    ⠀⣾⢻⣿⣿⠃⠀⠀⡀⢀⡄⠁⠀⠀⢠⡾ 
    ⠀⠃⢸⣿⡇⠀⢠⣾⡇⢸⡇⠀⠀⠀⡞ 
    ⠀⠀⠈⢿⡇⡰⠋⠈⠙⠂⠙⠢ 
    ⠀⠀⠀⠈⢧ 
    ______           __             __ 
   / ____/___  _  __/ /__________  / /_
  / /_  / __ \| |/_/ __/ ___/ __ \/ __/
 / __/ / /_/ />  </ /_/ /  / /_/ / /_  
/_/    \____/_/|_|\__/_/   \____/\__/  
                                       
    """ + Style.RESET_ALL)

def get_ip_info(ip):
    url = f"https://api.ip2location.io/?key={API_KEY}&ip={ip}&format=json"
    response = requests.get(url)
    return response.json()

def save_personal_data():
    personal_data = f""" 



                
 -----------------------------------------------------
    Основная информация
    ФИО: {input("ФИО: ")}
    Номер телефона: {input("Номер телефона: ")}
    Город: {input("Город: ")}
    Страна: {input("Страна: ")}
    Регион: {input("Регион: ")}
    Адрес проживания: {input("Адрес проживания: ")}
    ИНН: {input("ИНН: ")}
    Снилс: {input("Снилс: ")}
    Полис: {input("Полис: ")}
    -----------------------------------------------------
    Авто
    Марка автомобиля: {input("Марка автомобиля: ")}
    Номер автомобиля: {input("Номер автомобиля: ")}
    -----------------------------------------------------
    Банк
    Номер карты: {input("Номер карты: ")}
    -----------------------------------------------------
    Работа
    Занятость: {input("Занятость: ")}
    Адрес работы: {input("Адрес работы: ")}
    -----------------------------------------------------
    Интернет
    IP адрес: {input("IP адрес: ")}
    Город: {input("Город: ")}
    Провайдер: {input("Провайдер: ")}
    Широта: {input("Широта: ")}
    Долгота: {input("Долгота: ")}
    Страна: {input("Страна: ")}
    -----------------------------------------------------
    Соцсети/сервисы
    VK: {input("VK: ")}
    OK: {input("OK: ")}
    ТГ: {input("ТГ: ")}
    ДС: {input("ДС: ")}
    STEAM: {input("STEAM: ")}
    почта: {input("почта: ")}
    Instagram: {input("Instagram: ")}
    Facebook: {input("Facebook: ")}
    TikTok: {input("TikTok: ")}
    ----------------------------------------------------- 
    """
    
    with open("personal_data.txt", "w", encoding="utf-8") as file:
        file.write(personal_data)
    print(Fore.LIGHTGREEN_EX + "\nДанные успешно сохранены в personal_data.txt" + Style.RESET_ALL)


def main_menu():
    display_banner()
    while True:
        print("\n--- Главное меню ---")
        print(Fore.LIGHTYELLOW_EX + "1. Просмотреть информацию об IP        6. Стандартизация email" + Style.RESET_ALL)
        print(Fore.LIGHTYELLOW_EX + "2. Поиск по номеру телефона" + Style.RESET_ALL)
        print(Fore.LIGHTYELLOW_EX + "3. Информация про софт" + Style.RESET_ALL)
        print(Fore.LIGHTYELLOW_EX + "4. Шаблон для Информации о человеке" + Style.RESET_ALL)
        print(Fore.LIGHTYELLOW_EX + "5. Запустить поиск" + Style.RESET_ALL)
        print(Fore.LIGHTYELLOW_EX + "0. Выход" + Style.RESET_ALL)

        choice = input(Fore.LIGHTYELLOW_EX + "Выберите опцию (1-5): " + Style.RESET_ALL)

        if choice == "1":
            ip = input(Fore.LIGHTGREEN_EX + "Введите IP-адрес: " + Style.RESET_ALL)
            info = get_ip_info(ip)
            print(Fore.LIGHTGREEN_EX + f"Информация об IP: {info}" + Style.RESET_ALL)
        elif choice == "2":
            os.system("python foxphone.py")
        elif choice == "3":
            print("\nВерсия софта: 1.0")
            print("\nСоздатели: kokosikov")
            print(Fore.RED + "\nВнимание! Мы не ответственны за ваши действия данного софта, так что пользуйтесь с умом ;)")
        elif choice == "4":
            save_personal_data()

        elif choice == "5":
            os.system("python foxsearch.py")
        elif choice == "6":
            os.system("python foxmail.py")
        elif choice == "0":
            print("\nВыход из программы. До свидания!")
            break
        else:
            print("\nНеправильный выбор. Попробуйте снова.")

# Запуск программы
main_menu()
