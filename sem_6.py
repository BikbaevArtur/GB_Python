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
import random

size_1 = int(input("Input size list_1: "))
# size_2 = int(input("Input size list_2: "))
list_1 = [random.randint(1, 10) for _ in range(size_1)]
print(list_1)
list_2 = [random.randint(1, 10) for _ in range(size_1)]
print(list_2)
list_3 = []

for i in range(size_1):
    if list_1[i] in list_3:
        list_3.append(list_1[i])
print(list_3)