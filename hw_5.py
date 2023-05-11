# Урок 5. Рекурсия и алгоритмы
# Задача 26:  Напишите программу, которая на вход принимает два числа A и B, и возводит число А в целую степень B с помощью рекурсии.

# *Пример:*

# A = 3; B = 5 -> 243 (3⁵)
#     A = 2; B = 3 -> 8 

# def power_recursive(A, B):
#     if B == 0:
#         return 1
#     elif B > 0:
#         return A * power_recursive(A, B - 1)
#     else:
#         return 1 / (A * power_recursive(A, -B - 1))
    
# A = int(input("Введите число: "))
# B = int(input("Введите степень: "))
# result = power_recursive(A, B)
# print(result)

# Задача 28: Напишите рекурсивную функцию sum(a, b), возвращающую сумму двух целых неотрицательных чисел. Из всех арифметических операций допускаются только +1 и -1. Также нельзя использовать циклы.

# *Пример:*

# 2 2
#     4 

def sum(a, b):
    if b == 0:
        return a
    elif b > 0:
        return sum(a + 1, b - 1)
    else:
        return sum(a - 1, b + 1)
    
A = int(input("Введите числоn 1 : "))
B = int(input("Введите число 2 : "))
result = sum(A, B)
print(result)