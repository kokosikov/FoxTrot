from dadata import Dadata

# Встроенные ключи
token = "ea7f66782aeed84b1cc00004a51eacfc87dc8fdb"
secret = "fd3c98dfa7545dc6f59a0188cd43a9de51a02b9a"

def main():
    dadata = Dadata(token, secret)
    
    # Ввод данных для проверки
    query = input("Введите серию и номер паспорта: ")
    
    # Используем метод clean для проверки данных паспорта
    try:
        result = dadata.clean("passport", query)
        print("Результат проверки:")
        print(result)
    except Exception as e:
        print(f"Произошла ошибка: {e}")
    
    print("Работа программы завершена.")

if __name__ == "__main__":
    main()
