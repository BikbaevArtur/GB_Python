# Урок 3. Списки и словари

# Задача 16: Требуется вычислить, сколько раз встречается некоторое число X в массиве A[1..N].
#  Пользователь в первой строке вводит натуральное число N – количество элементов в массиве.
# В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X

# *Пример:*

# 5
#     1 2 3 4 5
#     3
#     -> 1


# Задача 18: Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X. Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X

# *Пример:*

# 5
#     1 2 3 4 5
#     6
#     -> 5

# import random


# def new_array(size):
#     array = [random.randint(1, 10) for i in range(size)]
#     return array


# def search_num(array, num):
#     count = 0

#     for i in range(len(array)):
#         if array[i] == num:
#             count += 1

#     return count


# def nearest_num(array, num):
#     arr_length = len(array)
#     nearest_num = array[0]
#     diff = abs(num - nearest_num)
#     for i in range(1, arr_length):
#         curr_diff = abs(num - array[i])
#         if curr_diff < diff:
#             diff, nearest_num = curr_diff, array[i]

#     return nearest_num


# size = int(input("Input size list: "))
# num_search = int(input("Input num: "))

# new_list = new_array(size)
# print(new_list)
# result = search_num(new_list, num_search)

# if result > 0:
#     print(f"число {num_search} встречается {result} раз")
# else:
#     nearest = nearest_num(new_list, num_search)
#     print(f"числа {num_search} нету в списке, ближайшее число {nearest}")


# *Задача 20: * В настольной игре Скрабл (Scrabble) каждая буква имеет определенную ценность.
#  В случае с английским алфавитом очки распределяются так:
# A, E, I, O, U, L, N, S, T, R – 1 очко;
#  D, G – 2 очка; B, C, M, P – 3 очка;
# F, H, V, W, Y – 4 очка; K – 5 очков;
# J, X – 8 очков;
# Q, Z – 10 очков.


# А русские буквы оцениваются так:
#  А, В, Е, И, Н, О, Р, С, Т – 1 очко;
#  Д, К, Л, М, П, У – 2 очка;
# Б, Г, Ё, Ь, Я – 3 очка;
#  Й, Ы – 4 очка;
# Ж, З, Х, Ц, Ч – 5 очков;
# Ш, Э, Ю – 8 очков;
# Ф, Щ, Ъ – 10 очков.


#  Напишите программу, которая вычисляет стоимость введенного пользователем слова.
# Будем считать, что на вход подается только одно слово, которое содержит либо только английские, либо только русские буквы.

# *Пример:*

# ноутбук
#     12

scrabble = {1:'AEIOULNSTRАВЕИНОРСТ',
            2:'DGДКЛМПУ',
            3:'BCMPБГЁЬЯ',
            4:'FHVWYЙЫ',
            5:'KЖЗХЦЧ',
            8:'JXШЭЮ',
            10:'QZФЩЪ' }
text = list(input("input text: ").upper())

sum = 0
for i in range(len(text)):
    for kay,value in scrabble.items():
        for letter in value:
            if text[i] == letter:
                sum += kay

print(sum)