"""
Урок 1. Ввод-Вывод, операторы ветвления
Задача 2: Найдите сумму цифр трехзначного числа.

*Пример:*

123 -> 6 (1 + 2 + 3)
100 -> 1 (1 + 0 + 0) |

def sum_digit(digit):
    sum = 0
    while digit > 0:
        num = digit % 10 
        sum = num+sum
        digit = digit // 10
    return sum
        

import random

digit = random.randint(100, 999)
print(digit)
print(sum_digit(digit)) 
"""


"""
Задача 4: Петя, Катя и Сережа делают из бумаги журавликов. Вместе они сделали
 S журавликов. Сколько журавликов сделал каждый ребенок, если известно, 
 что Петя и Сережа сделали одинаковое количество журавликов, 
 а Катя сделала в два раза больше журавликов, чем Петя и Сережа вместе?

*Пример:*

6 -> 1  4  1
24 -> 4  16  4
    60 -> 10  40  10


total = int(input("total quantiti of cranes: "))
kate = total // 2
serj = kate // 2
petr = serj
print(f"Kate made {kate} cranes, Serj and Petr made {serj} cranes ")
"""


"""
Задача 6: Вы пользуетесь общественным транспортом? Вероятно, вы расплачивались 
за проезд и получали билет с номером. Счастливым билетом называют такой билет с шестизначным номером
, где сумма первых трех цифр равна сумме последних трех. Т.е. билет с номером 385916 – счастливый, 
т.к. 3+8+5=9+1+6. Вам требуется написать программу, которая проверяет счастливость билета.

*Пример:*

385916 -> yes
123456 -> no


ticket_num = input("input ticket number: ")

sum_1 = 0
sum_2 = 0

ticket_array = [int(dig) for dig in str(ticket_num)]
length_ticket = len(ticket_array)

for i in range (length_ticket // 2 ):
    sum_1 = ticket_array[i]+sum_1
for j in range (length_ticket //2 , length_ticket):
    sum_2 = ticket_array[j]+sum_2

if sum_1 == sum_2:
    print(f"{ticket_num} - lucky ticket ")
else:
    print(f"{ticket_num} - unlucky ticket ")
   
"""

"""
Задача 8: Требуется определить, можно ли от шоколадки размером n × m долек отломить k долек, 
если разрешается сделать один разлом по прямой между дольками (то есть разломить шоколадку на два прямоугольника).

*Пример:*

3 2 4 -> yes
3 2 1 -> no


"""
chocolate_width = int(input("input chocolate bar width: "))
chocolate_length = int(input("input chocolate bar length: "))
divide_slices = int(input("input the number of slices: "))
number_slices = (chocolate_length*chocolate_width) - divide_slices
if number_slices % chocolate_length == 0 or number_slices % chocolate_length == 0:
    print("The chocolate bar can be divided")
else:
    print("The chocolate bar can not be divided")
