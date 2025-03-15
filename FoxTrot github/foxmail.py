from dadata import Dadata
import colorama
from colorama import Fore, Style
import re
colorama.init(autoreset=True)

# Ваши токены для работы с Dadata
TOKEN = "ea7f66782aeed84b1cc00004a51eacfc87dc8fdb"
SECRET = "fd3c98dfa7545dc6f59a0188cd43a9de51a02b9a"

# Инициализация Dadata
dadata = Dadata(TOKEN, SECRET)

def standardize_email_with_dadata(email):
    # Приведение email к стандартному формату
    email = email.strip().lower()
    email = re.sub(r'[^\w.-@]', '', email)
    
    # Запрос к Dadata
    try:
        result = dadata.clean("email", email)
        return {
            "source": result.get("source", ""),
            "email": result.get("email", ""),
            "local": result.get("local", ""),
            "domain": result.get("domain", ""),
            "type": result.get("qc_description", ""),
            "qc": result.get("qc", "")
        }
    except Exception as e:
        return {"error": f"Ошибка при работе с Dadata: {str(e)}"}

def main():

    email_input = input("Введите email: ")
    result = standardize_email_with_dadata(email_input)
    print("\nРезультат стандартизации:")
    for key, value in result.items():
        print(f"{key}: {value}")

if __name__ == "__main__":
    main()
