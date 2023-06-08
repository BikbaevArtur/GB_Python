from contact_manager import *

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