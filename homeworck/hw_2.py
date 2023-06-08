"""
Задача 10: На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – 
гербом. Определите минимальное число монеток, которые нужно перевернуть, чтобы все монетки 
были повернуты вверх одной и той же стороной. Выведите минимальное количество монет, которые нужно перевернуть
"""

# import random

# num_coins = int(input("int the numbers coins: "))
# count_tails = 0
# count_eagle = 0
# for i in range(num_coins):
#     coins_tails_eagle = random.randint(0, 1)
#     if coins_tails_eagle == 0:
#         count_tails += 1
#     else:
#         count_eagle += 1
# if count_tails < count_eagle:
#     print(f"min flip = {count_tails}")
# else:
#     print(f"min flip = {count_eagle}")

# ________________________________________

# Решение массивом
# def coins(num):
#     coin = [random.randint(0, 1) for _ in range(num)]
#     return coin


# def result(coin):
#     count_tails = 0
#     count_eagle = 0
#     for i in range(len(coin)):
#         if coin[i] == 1:
#             count_tails += 1
#         else:
#             count_eagle += 1
#     return count_tails, count_eagle

# num_coin = int(input("input the numbers coins: "))
# array = coins(num_coin)
# print(array)
# tails, eagle = result(array)
# if tails < eagle:
#     print(f"flip a coin{tails}")
# else:
#     print(f"flip a coin {eagle}")


"""
Задача 12: Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница. Петя помогает 
Кате по математике. Он задумывает два натуральных числа X и Y (X,Y≤1000), а Катя должна их отгадать.
 Для этого Петя делает две подсказки. Он называет сумму этих чисел S и их произведение P. 
 Помогите Кате отгадать задуманные Петей числа.
"""
# import random
# x = random.randint(1,1000)
# y = random.randint(1,1000)
# for i in range (1000):
#     for j in range (1000):
#         if x*y == i*j and x+y==i+j:
#             print(i,j)






"""

Задача 14: Требуется вывести все целые степени двойки (т.е. числа вида 2k), не превосходящие числа N.
"""


# num = int(input("input number "))
# i = 1
# while 2**i < num:
#     print(2**i)
#     i += 1
