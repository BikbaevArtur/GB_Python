# Задача №33. Решение в группах
# Хакер Василий получил доступ к классному журналу и
# хочет заменить все свои минимальные оценки на
# максимальные. Напишите программу, которая
# заменяет оценки Василия, но наоборот: все
# максимальные – на минимальные.
# Input: 5 -> 1 3 3 3 4
# Output: 1 3 3 3 1

# def grade(size):
#     import random
#     grade = [random.randint(1,5) for _ in range(size)]
#     return grade

# def grade_creat(grade):
#     grade_min = min(grade)
#     grade_max = max(grade)
#     for i in range(len(grade)):
#         if grade[i] == grade_max :
#             grade[i] = grade_min
#     return grade


# grade_num = grade(10)
# print(grade_num)
# creat_grate = grade_creat(grade_num)
# print(creat_grate)

    

# Задача №35. Решение в группах
# Напишите функцию, которая принимает одно число и
# проверяет, является ли оно простым
# Напоминание: Простое число - это число, которое
# имеет 2 делителя: 1 и n(само число)
# Input: 5
# Output: yes


# def inspect_num(num):
#     count = 0
#     for i in range(1,num+1):
#         if num % i == 0:
#             count += 1
#     return count

number = int(input("input num: "))
# result = inspect_num(number)
# if result == 2:
#     print("Простое число")
# else:
#     print("сложное число")

def is_simple(num: int) -> bool:
    if num in [1,2]:
        return True
    for i in range(3,num//2 +1 , 2):
        if num%i ==0:
            return False
        return True

print(is_simple(number))