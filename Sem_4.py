# import random 

# size = int(input('Введите размер вашего списка: '))
# min_limit = int(input('Введите минимальный предел: '))
# max_limit = int(input('Введите максимальный предел: '))

# my_list = [random.randint(min_limit, max_limit) for _ in range(size)]
# print(my_list)
# number = int(input('Введите искомое число: '))

# count = my_list.count(number)

# closest = my_list[0]
# if count <= 0 :
#     for item in my_list:
#         if abs(item - number) < abs(number-closest):
#             closest = item
# print(f'Число {number} встречается {count} раз' if count > 0 else f'Ближайшее к {number} число - {closest}')

# Задача №25. Решение в группах
# Напишите программу, которая принимает на вход
# строку, и отслеживает, сколько раз каждый символ
# уже встречался. Количество повторов добавляется к
# символам с помощью постфикса формата _n.
# Input: a a a b c a a d c d d
# Output: a a_1 a_2 b c a_3 a_4 d c_1 d_1 d_2
# Для решения данной задачи используйте функцию
# .split()

# text = list(input('Введите строку: '))     
# count_dict = {}
# for letter in text:
#     count_dict[letter] = count_dict.get(letter,0)+1
#     print(f'{letter}' if count_dict.get(letter) == 1 else f'{letter}_{count_dict.get(letter)-1}', end=' ')