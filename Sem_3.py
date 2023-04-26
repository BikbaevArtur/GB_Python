# Задача No17. Решение в группах
# Дан список чисел. Определите, сколько в нем
# встречается различных чисел.
# Input: [1, 1, 2, 0, -1, 3, 4, 4]
# Output: 6
# import random


# def list_1(size):
#     new_list = [random.randint(1, 10) for i in range(size)]
#     return new_list


# def output_num(list_1):
#     return len(set(list_1)) # мы создаем множество из словаря, в множество могут быть только уникальыне значения,
#                             # потом смотрим длинну множество

# size = int(input("input size list: "))
# n_list = list_1(size)
# result = output_num(n_list)
# print(n_list)
# print(result)


# Задача No19. Решение в группах
# Дана последовательность из N целых чисел и число
# K. Необходимо сдвинуть всю последовательность
# (сдвиг - циклический) на K элементов вправо, K –
# положительное число.
# Input: [1, 2, 3, 4, 5] k = 3
# Output: [4, 5, 1, 2, 3]
import random


def list_1(size):
    new_list = [random.randint(1, 10) for i in range(size)]
    return new_list


def correct_list(creat_list):
    length_list  = len(creat_list)-1 
    for i in range(length_list):
        creat_list[i],creat_list[i+1] = creat_list[i+1],creat_list[i]
    return creat_list

size = int(input("input size list: "))
n_list = list_1(size)
c_list = correct_list(n_list)
print(n_list)
print(c_list)
# Семинар 3. Списки и словари
# Задача No21. Решение в группах
# Напишите программу для печати всех уникальных
# значений в словаре.
# Input: [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"},
# {"VI": "S005"}, {"VII": " S005 "}, {" V ":" S009 "}, {" VIII
# ":" S007 "}]
# Output: {'S005', 'S002', 'S007', 'S001', 'S009'}


# Семинар 3. Списки и словари
# Задача No23. Решение в группах
# Дан массив, состоящий из целых чисел. Напишите
# программу, которая подсчитает количество
# элементов массива, больших предыдущего (элемента
# с предыдущим номером)
# Input: [0, -1, 5, 2, 3]
# Output: 2 (-1 < 5, 2 < 3)
