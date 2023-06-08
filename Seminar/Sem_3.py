# Задача No17. Решение в группах
# Дан список чисел. Определите, сколько в нем
# встречается различных чисел.
# Input: [1, 1, 2, 0, -1, 3, 4, 4]
# Output: 6

# import random
# list_1 = list(input("введите значения, превращает 123154 в '1' '2' '3' '4' "))


# def list_1(size):
#     new_list = [random.randint(1, 10) for i in range(size)]
#     return new_list


# def output_num(list_1):
#     # мы создаем множество из словаря, в множество могут быть только уникальыне значения,
#     return len(set(list_1))
#     # потом смотрим длинну множество


# def uniq_list(list_new):
#     uniq_list = []
#     for item in list_new:
#         if not item in uniq_list:
#             uniq_list.append(item)
#     return uniq_list


# size = int(input("input size list: "))
# n_list = list_1(size)
# result = output_num(n_list)
# print(n_list)
# print(result)
# print(uniq_list(n_list))


# Задача No19. Решение в группах
# Дана последовательность из N целых чисел и число
# K. Необходимо сдвинуть всю последовательность
# (сдвиг - циклический) на K элементов вправо, K –
# положительное число.
# Input: [1, 2, 3, 4, 5] k = 3
# Output: [4, 5, 1, 2, 3]


# import random

# list_1 = [random.randint(1, 10) for i in range(5)]
# print(list_1)
# k = int(input("Кол во эл на сдвиг: "))
# list_1 = list_1[-k:]+ list_1[:-k]

# print(list_1)

# Семинар 3. Списки и словари
# Задача No21. Решение в группах
# Напишите программу для печати всех уникальных
# значений в словаре.
# Input: [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"},
# {"VI": "S005"}, {"VII": " S005 "}, {" V ":" S009 "}, {" VIII
# ":" S007 "}]
# Output: {'S005', 'S002', 'S007', 'S001', 'S009'}


my_list = [    {"V": "S001"}, {"V": "S002"},    {"VI": "S001"}, {"VI": "S005"},    {"VII": "S005"}, {"V": "S009"},    {"VIII": "S007"}]

uniq = set()
for items in my_list:
    for val in items.values():
        uniq.add(val)
print(uniq)

    
          


# Семинар 3. Списки и словари
# Задача No23. Решение в группах
# Дан массив, состоящий из целых чисел. Напишите
# программу, которая подсчитает количество
# элементов массива, больших предыдущего (элемента
# с предыдущим номером)
# Input: [0, -1, 5, 2, 3]
# Output: 2 (-1 < 5, 2 < 3)



# import random

# array = [random.randint(1,10) for i in range(10)]
# count = 0
# for i in range(len(array)-1):
#     if array[i] > array[i+1]:
#         count += 1
# print(f"{array} \n количетсво эл {count}")
