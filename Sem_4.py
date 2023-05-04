import random 

size = int(input('Введите размер вашего списка: '))
min_limit = int(input('Введите минимальный предел: '))
max_limit = int(input('Введите максимальный предел: '))

my_list = [random.randint(min_limit, max_limit) for _ in range(size)]
print(my_list)
number = int(input('Введите искомое число: '))

count = my_list.count(number)

closest = my_list[0]
if count <= 0 :
    for item in my_list:
        if abs(item - number) < abs(number-closest):
            closest = item
print(f'Число {number} встречается {count} раз' if count > 0 else f'Ближайшее к {number} число - {closest}')

