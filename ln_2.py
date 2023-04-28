# list_1 = []
# list_1 = list()
# list_1 = [1,2,3,4,]
# print(list_1) #  можно раскрыть список с помощью знака *

# for i in list_1:
#     print(i)

# print(len(list_1))

# list_1 = [1,5]
# print(list_1)
# list_1.append(8)  #append - дополнение к списку
# print(list_1)


# import random
# list_1 = []
# for i in range(5):
#     list_1.append(random.randint(1,10)) # заполнение списка
# print(list_1)

# list_1 = [12,7,-1,21,0]
# print(list_1.pop()) # pop удаляет последнее значение списка, возвращает элемент и удаляет его со списка
# print(list_1)
# print(list_1.pop()) # pop(1) 1- индекс элемента
# print(list_1)
# print(list_1.pop())
# print(list_1)
# print(list_1.pop())
# print(list_1)

# # добовление элемента на нужную позицию
# list_1 = [12, 7, -1, 21, 0]
# print(list_1.insert(2, 11))
# print(list_1) # [12, 7, 11, -1 ,21, 0]   добавляет на 2 позицию элемент 11

# list_1 = [12, 7, 1, 21, 2, 1, 3, 5, 6, 7]
# print(list_1[1])
# print(list_1[:2]) #срез элементов выводим первые два элемента
# print(list_1[len(list_1)-2 :]) #выводим два последних элемента
# print(list_1[2:9]) # выводим от 2 элемента до 9
# print(list_1[::6])# вывод с шагом 6

# Кортеж - неизменяемый список, работает быстрее чем обычный списов, кортеж занимает меньше место
# использование, для защиты данных
# t = ()  # создание кортежа
# print(type(t))  # clsaa <tuple>

# t = (1, )  # нужно в конце ставить запятую
# print(type(t))

# v = [1, 2, 3]
# print(v)
# print(type(v))

# v = tuple(v)  #преобразование списка в кортеж

# print(v)
# print(type(v))

# a,b,c = v # распоковка кортежа, присвоили к переменным, значение кортежа
# print(a,b,c)

# Словари - неупорядочные колекции произвольных объектов с доступом по ключу
# в списках в качестве ключа используются индекс элемента. В словаре для определение 
# элемента используются значения ключа(строка, число)

d = {} # создание словаря
d = dict() # создание словаря 
d['q'] = 'qwerty'
# print(d)
d['w'] = 'werty'
# print(d)
# print(d['q']) # 
# del d['q'] # deleted key d 
# for i in d:
#     print('{}:{}' .format(i,d[i])) # 
# #так де можно 
for (kay,val) in d.items():
    print(kay,val)

#  Множество содержит в себе уникальные элементы, не обязательно упорядочные 
# Одно множество может содержать значения любых типов, Если у вас два множество 
# Вы можете совершать над ним любые стандартные операции, например объеденение,
# пересечение  и разность. 

# color = {'red', 'green', 'blue'}
# print(color)
# color = {'red', 'green', 'blue'}
# color.add('red')
# print(color)
# color.add('grey')
# print(color)
# color.remove('red')
# print(color)
# color.discard('red')#проверяет, есть ли red, если есть, удаляет
# print(color)
# color.clear()#удаление полностью
# print(color)

# q=set() #создание множество

# операции с множествами

# a={1, 2, 3, 4, 5}
# b={2, 5, 6, 7, 2}
# # c = a.copy()# копирование множество
# # u = a.union(b) #объяденить множество уникальное значение
# # i = a.intersection(b) # пересечение, тобишь одинаковые значения
# # dl = a.difference(b)# разница а и б
# q = a.union(b).difference(a.intersection(b))
# print(q)

# a = {1, 8, 6}
# b = frozenset(a) # фиксация множество

# List Comprehension
# У каждого языка проограммирование есть свои особенности, и преймущества.
# Одна из культовых фишет Python - list comprehension(генератор списка)
# Comprehensions лугко читать и их используют как начинающие, так и опытные разработчики. list comprehension это упрощенный 
# подход к созданию списка который задействует цикл for а также инструкции if else 
# для опреедение того что в итоге окажется фатальном списке
# 1. простая ситуация - список:
# list_1 = [exp for item in iterebale]
# 1. выбрать по ззаданному условию
# list_1 = [exp for item in iterebale(if conditional)]

# list_1 = [i for i in range(1,101)] # пополняем список 1 до 100
# print(list_1)

# list_1 = [i for i in range(1,101) if i % 2 == 0] # Добавили условие, на четные числа
# print(list_1)

# list_1 = [(i,i) for i in range(1,101)] # можно создать кортеж
# print(list_1) 

