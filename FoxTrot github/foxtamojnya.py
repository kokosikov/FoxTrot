from dadata import Dadata

# Встроенные ключи
token = "ea7f66782aeed84b1cc00004a51eacfc87dc8fdb"
secret = "fd3c98dfa7545dc6f59a0188cd43a9de51a02b9a"

def full_text_search(dadata, query):
    # Здесь можете адаптировать к реальным запросам DaData (пример на основе очистки ФИО)
    return dadata.suggest("fio", query)

def get_record_by_id(dadata, record_id):
    # Пример получения записи по идентификатору (может быть адаптировано к реальным запросам DaData)
    return dadata.find_by_id("party", record_id)

def main():
    dadata = Dadata(token, secret)

    print("Выберите действие:")
    print("1. Полнотекстовый поиск")
    print("2. Запись справочника по идентификатору")
    choice = input("Введите номер действия (1 или 2): ")

    if choice == "1":
        query = input("Введите поисковой запрос: ")
        try:
            result = full_text_search(dadata, query)
            print("Результат полнотекстового поиска:")
            print(result)
        except Exception as e:
            print(f"Произошла ошибка: {e}")
    elif choice == "2":
        record_id = input("Введите идентификатор записи: ")
        try:
            result = get_record_by_id(dadata, record_id)
            print("Результат запроса по идентификатору:")
            print(result)
        except Exception as e:
            print(f"Произошла ошибка: {e}")
    else:
        print("Некорректный выбор. Пожалуйста, выберите 1 или 2.")

if __name__ == "__main__":
    main()
