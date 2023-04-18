# my_limit = int(input("Fact "))
# fact = 1
# count = 1 
# while count <= my_limit:
#     fact *= count
#     count += 1
# print(fact)

# дано натуральное число A > 1. Определить, каким по счету числом фибоначи оно явлется
# то есть выведите такое число n, что f(n) = A. Если A не является числом фибоначи, выведите -1

# n1 = 0
# n2 =1 
# k = 2
# a = int(input())
# while n2 < a:
#     n1,n2 = n2,n1+n2
#     k +=1
#     print(n2)
# if n2 != a:
#     print("-1")
# else:
#     print(k)

# Уставшие от необычно теплой зимы, жители решили узнать, 
# действительно ли это самая длинная оттепель за всю историю наблюдений за погодой. 
# Они обратились к синоптикам, а те, в свою очередь, занялись исследованиями статистики за прошлые годы.
# Их интересует, сколько дней длилась самая длинная оттепель. 
# Оттепелью они называют период, в который среднесуточная температура ежедневно превышала 0 градусов Цельсия. 
# Напишите программу, помогающую синоптикам в работе. 

# import random 

# length_day = 30
# temp_day = 0
# count = 0
# max_count = 0
# for i in range(1,length_day+1):
#     temp_day += random.randint(-3,3)
#     if temp_day >= 0:
#         count += 1
#     else:
#         if count > max_count:
#             max_count = count
#         count = 0
#     print(f"day {i} temp = {temp_day}")
# print(f"{count} day is > 0 ")


# import random
# num_wotermelon = int(input("Enter nums the wotermelon: "))
# wotrmelon_for_me = 0
# wotrmelon_for_mother_in_law = 20000
# for i in range(num_wotermelon):
#     wotermelon = random.randint(1000, 20000)
#     if wotermelon > wotrmelon_for_me:
#         wotrmelon_for_me = wotermelon
#     elif wotermelon < wotrmelon_for_mother_in_law:
#         wotrmelon_for_mother_in_law = wotermelon
#     print (wotermelon, end = " ")
# print(f"\nwotrmelon for me:{wotrmelon_for_me}, wotermelon for mother-in-law {wotrmelon_for_mother_in_law} ")

