# my_limit = int(input("Введите факторияал "))
# fact = 1
# count = 1

# while count <= my_limit:
#     fact *= count
#     count += 1
# print(fact)


# Дано натуральное число > 1 определите каким по счету фибоначи оно является

def fib_true_false(num):
    fib = [0, 1]
    i = 2
    for i in range(1, 1000):
        if fib[i] <= num:
            fib.append(fib[i-1]+fib[i-2])
        elif num == fib[i]:
            print("+")
            return True
        else:
            print("-")
            return False
    

fib_true_false(29)
