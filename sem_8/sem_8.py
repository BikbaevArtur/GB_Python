# Создать телефонный справочник с возможностью импорта и экспорта данных в формате .txt. Фамилия, имя, отчество, номер телефона - данные, которые должны находиться в файле.

# 1. Программа должна выводить данные
# 2. Программа должна сохранять данные в текстовом файле
# 3. Пользователь может ввести одну из характеристик для поиска определенной записи(Например имя или фамилию человека)
# 4. Использование функций. Ваша программа не должна быть линейной

# 10:03
# 1. Открыть файл
# 2. Сохранить файл
# 3. Показать тк
# 4. Добавить контакт
# 5. Найти контакт
# 6. Изменить контакт
# 7. Удалить контакт
# 8. Выход

path = 'phonebook.txt'

# def menu_phonemook():
#     print("1.Открыть файл \n2.Сохранить файл \n3.Показать тк \n4.Добавить контакнт \n5.Найти контакт \n6.Изменить контакт \n7.Удалить контакт \n8.Выход")
#     button = input("Выберите пункт меню")
#     while 
def creat_open_file():
    data = open(path, 'r', encoding='UTF-8')
    data.close

def addint_intro_file():
    data = open(path, 'a', encoding='UTF-8')
    name = input("Введите имя: ").capitalize()
    middle_name = input("Введите отчество: ").capitalize()
    sur_name = input("Введите фамилию: ").capitalize()
    phone = input("Введите номер телефона: ").capitalize()
    data.write(f"{name} {middle_name} {sur_name} {phone}")

def readint_file():
    data = open(path, 'r', encoding='UTF-8')
    print(data.read())
    data.close()

def finding_contact_file():
    data = open(path, 'r', encoding='UTF-8')
    finding_contact = input("Введите искомый параметр: ")
    i_find_it = data.readlines()
    dict_contacts = {}
    for i, j in enumerate(i_find_it,1):
        j = j.strip()
        dict_contacts = {'name': i_find_it[0], 'middle_name': i_find_it[1], 'sur_name' : i_find_it[2], 'phone': i_find_it[3] }
    for item in i_find_it:
        if item  == finding_contact:
            print()

# menu_phonemook()



# path = 'phonebook.txt'


# def add_contact():
#     with open('phone_book.txt', 'a', encoding='UTF-8') as data:
#         new_contact = str(input("Введи новый контакт: "))
#         new_contact = new_contact + '\n'
#         data.writelines(new_contact)
#     return 'Контакт добавлен'


# def clear_all():
#     with open('phone_book.txt', 'w', encoding='UTF-8') as data:
#         data.write('')


# def faind_contact():
#     with open('phone_book.txt', 'r+', encoding='UTF-8') as file1:
#         data_list = []
#         for line in file1:
#             data_list.append(line.strip())
#         print(data_list)
#         for i in data_list:
#             res = i.split()
#             if res[0] == 'Алексей':
#                 print("Нашли")


# def main_func():
#     print('1 - добавить контакт')
#     print('2 - закрыть книгу')
#     print('3 - очистить книгу')
#     print('4 - найти контакт')
#     while True:
#         menu = int(input('Действие: '))

#         if menu == 1:
#             print(add_contact())
#         elif menu == 2:
#             break
#         elif menu == 3:
#             clear_all()
#         elif menu == 4:
#             faind_contact()


# main_func()

# with open('phone_book.txt', 'r', encoding='UTF-8') as data:
#     res = data.read()
#     print(res)