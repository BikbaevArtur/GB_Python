# # Создать телефонный справочник с возможностью импорта и экспорта данных в формате .txt. Фамилия, имя, отчество, номер телефона - данные, которые должны находиться в файле.

# # 1. Программа должна выводить данные
# # 2. Программа должна сохранять данные в текстовом файле
# # 3. Пользователь может ввести одну из характеристик для поиска определенной записи(Например имя или фамилию человека)
# # 4. Использование функций. Ваша программа не должна быть линейной

# # 10:03
# # 1. Открыть файл
# # 2. Сохранить файл
# # 3. Показать тк
# # 4. Добавить контакт
# # 5. Найти контакт
# # 6. Изменить контакт
# # 7. Удалить контакт
# # 8. Выход

def import_contacts(file_name):
    contacts = []
    try:
        with open(file_name, 'r', encoding='UTF-8') as file:
            for line in file:
                data = line.strip().split(',')
                contact = {
                    'last_name': data[0],
                    'first_name': data[1],
                    'middle_name': data[2],
                    'phone_number': data[3]
                }
                contacts.append(contact)
    except FileNotFoundError:
        print("Файл не найден.")
    return contacts

def export_contacts(contacts, file_name):
    try:
        with open(file_name, 'w', encoding='UTF-8') as file:
            for contact in contacts:
                line = f"{contact['last_name']},{contact['first_name']},{contact['middle_name']},{contact['phone_number']}\n"
                file.write(line)
        print("Данные сохранены в файле.")
    except:
        print("Ошибка сохранения данных в файле.")

def add_contact(contacts, contact):
    contacts.append(contact)
    print("Контакт добавлен.")



def display_contact(contact):
    print(f"Фамилия: {contact['last_name']}")
    print(f"Имя: {contact['first_name']}")
    print(f"Отчество: {contact['middle_name']}")
    print(f"Номер телефона: {contact['phone_number']}")
    print()

def display_contacts(contacts):
    if contacts:
        print("Список контактов:")
        for contact in contacts:
            display_contact(contact)
    else:
        print("Нет данных для отображения.")

def search_contacts(contacts, search_key):
    results = []
    for contact in contacts:
        if (search_key.lower() in contact['last_name'].lower()) or (search_key.lower() in contact['first_name'].lower()) or (search_key.lower() in contact['middle_name'].lower()):
            results.append(contact)
    return results

def create_contact():
    last_name = input("Введите фамилию: ")
    first_name = input("Введите имя: ")
    middle_name = input("Введите отчество: ")
    phone_number = input("Введите номер телефона: ")

    return {
        'last_name': last_name,
        'first_name': first_name,
        'middle_name': middle_name,
        'phone_number': phone_number
    }



def main_menu():
    print("1. Просмотреть контакты")
    print("2. Добавить контакт")
    print("3. Сохранить контакты в файл")
    print("4. Поиск контактов")
    print("5. Выход")

def get_user_choice():
    return input("Введите номер операции: ")

def get_search_key():
    return input("Введите фамилию или имя для поиска: ")

def main():
    file_name = "contacts.txt"
    contacts = import_contacts(file_name)

    while True:
        main_menu()
        choice = get_user_choice()

        if choice == '1':
            display_contacts(contacts)
        elif choice == '2':
            contact = create_contact()
            add_contact(contacts, contact)
        elif choice == '3':
            export_contacts(contacts, file_name)
        elif choice == '4':
            search_key = get_search_key()
            results = search_contacts(contacts, search_key)
            display_contacts(results)
        elif choice == '5':
            break
        else:
            print("Ошибка, повторите ввод операции")  

main()