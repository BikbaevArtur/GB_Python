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

# добовление элемента на нужную позицию
list_1 = [12, 7, -1, 21, 0]
print(list_1.insert(2, 11))
print(list_1) # [12, 7, 11, -1 ,21, 0]   добавляет на 2 позицию элемент 11
