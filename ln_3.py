# def calc1(a, b):
#     return a+b


# def math(op, x, y):
#     print(op(x, y))


# math(lambda a, b: a+b, 5, 45)

# в списке хронятся числа. Нужно выбрать только четные числа и составить список пар(число, квадрат числа)
# a = 1
# my_list= [1,2,3,5,8,15,23,38]
# res = list()
# for item in my_list:
#     if item %2 ==0:
#         res.append((item,item**2))
# print(res)


def select(f,col):
    return[f(x) for x in col]

def where(f,col):
    return[x for x in col if f(x)]