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