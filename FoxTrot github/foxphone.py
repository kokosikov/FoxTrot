from dadata import Dadata

# Ваши токены для работы с Dadata
TOKEN = "ea7f66782aeed84b1cc00004a51eacfc87dc8fdb"
SECRET = "fd3c98dfa7545dc6f59a0188cd43a9de51a02b9a"

# Инициализация Dadata
dadata = Dadata(TOKEN, SECRET)

def standardize_phone_with_dadata(phone):
    # Приведение номера телефона к стандартному формату
    phone = phone.strip().replace(" ", "").replace("-", "").replace("(", "").replace(")", "")
    
    try:
        # Запрос к Dadata для очистки телефона
        result = dadata.clean("phone", phone)
        if result:
            standardized_phone = result.get("phone", "")
            return {
                "source": result.get("source", ""),
                "phone": standardized_phone,
                "type": result.get("qc_description", ""),
                "country_code": result.get("country_code", ""),
                "city_code": result.get("city_code", ""),
                "number": result.get("number", ""),
                "provider": result.get("provider", ""),
                "region": result.get("region", ""),
                "qc": result.get("qc", ""),
                "Telegram": f"https://t.me/{standardized_phone}",
                "Viber": f"https://adguardteam.github.io/AnonymousRedirect/redirect.html?url=viber://chat?number={standardized_phone}",
                "WhatsApp": f"https://wa.me/{standardized_phone}"
            }
    except Exception as e:
        return {"error": f"Ошибка при работе с Dadata: {str(e)}"}

def main():
    phone_input = input("Введите номер телефона: ")
    result = standardize_phone_with_dadata(phone_input)
    print("\nРезультат стандартизации:")
    for key, value in result.items():
        print(f"{key}: {value}")

if __name__ == "__main__":
    main()
