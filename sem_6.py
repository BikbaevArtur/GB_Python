# Даны два массива чисел. Требуется вывести те элементы
# первого массива (в том порядке, в каком они идут в первом
# массиве), которых нет во втором массиве. Пользователь вводит
# число N - количество элементов в первом массиве, затем N
# чисел - элементы массива. Затем число M - количество
# элементов во втором массиве. Затем элементы второго массива
# Ввод: Вывод:
# 7 3 3 2 12
# 3 1 3 4 2 4 12
# 6
# 4 15 43 1 15 1

# import random

# size_1 = int(input("Input size list_1: "))
# # size_2 = int(input("Input size list_2: "))
# list_1 = [random.randint(1, 10) for _ in range(size_1)]
# print(list_1)
# list_2 = [random.randint(1, 10) for _ in range(size_1)]
# print(list_2)
# list_3 = []

# for item in list_1:
#     if item not in list_2:
#         list_3.append(item)
# print(list_3)
#можно так
# list_3 = [i for i in list_1 if i not in list_2]

# Задача №41. Решение в группах
# Дан массив, состоящий из целых чисел. Напишите
# программу, которая в данном массиве определит
# количество элементов, у которых два соседних и, при
# этом, оба соседних элемента меньше данного. Сначала
# вводится число N — количество элементов в массиве
# Далее записаны N чисел — элементы массива. Массив
# состоит из целых чисел.
# import random
# list_one = [random.randint(1,10) for _ in range(10) ]
# print(list_one)
# count = 0
# for i in range(1,len(list_one)-1):
#     if list_one[i-1] < list_one[i] and list_one[i+1] < list_one[i]:
#         count += 1
# print(count)

# result = [1 for i in range(1,len(list_one)-1) if list_one[i-1]< list_one[i]>list_one[i+1]]
# print(len(result))

# Задача №43. Решение в группах
# Дан список чисел. Посчитайте, сколько в нем пар
# элементов, равных друг другу. Считается, что любые
# два элемента, равные друг другу образуют одну пару,
# которую необходимо посчитать. Вводится список
# чисел. Все числа списка находятся на разных
# строках

def list_array(min_val,max_val,size):
    import random
    new_list = [random.randint(min_val,max_val) for _ in range(size)]
    return new_list

# def double(min_val,max_val,list_serch):
#     while(min_val < max_val):
#         count =0
#         count_1 = 0
#         for i in range(len(list_serch)):
#             if min_val == list_serch[i]:
#                 count +=1
#         print(f'{min_val} : {count}')
#         min_val +=1
        
def uniq_dic(list_1):
    uniq_dict = {}
    for num in list_1:
        uniq_dict[num] = uniq_dict.get(num,0)+1
    print(uniq_dict)
    return uniq_dict


list_1 = list_array(1,10,10)
print(list_1)
uniq_dic(list_1)
