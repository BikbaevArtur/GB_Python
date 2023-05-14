# def sumnumbers(n):
#     summ =0
#     for i in range(1, n+1):
#         summ += i
#     print(summ)

# sumnumbers(5)

# def sum_str(*args):  #(*args) неограниченное кол во аргументов
#     res = ''
#     for i in args:
#         res += i
#     return res

# print(sum_str('q', 'e', 'l'))

# import modul1

# print(modul1.max1(5,9))

# from modul1 import max1  тот же  вариант, но не надо писать modul1

# print(max1(9,10))

# from modul1 import * b

# import modul1 as m1  изменяем название modul1 на время применение на m1

# def fib(n):
#     if n in [1,2]:
#         return 1
#     return fib(n-1)+fib(n-2)
# list_1 = []
# for i in range(1,10):
#     list_1.append(fib(i))
# print(list_1)

# def quick_sort(array):   #быстрая сортировка
#     if len(array) <= 1:
#         return array
#     else:
#         privot = array
#     less = [i for i in array[1:]if i <= privot]
#     greatet = [i for i in array[1:] if i > privot]
#     return quick_sort(less) + [privot] + quick_sort(greatet)

# print(quick_sort([1,5,6,2,77,123,11]))

def merge_sort(nums):
    if len(nums) > 1:
        mid = len(nums) //2
        left = nums[:mid]
        right = nums[mid:]
        merge_sort(left)
        merge_sort(right)
        i=j=k=0
        while i<len(left) and j<len(right):
            if left[i] < right[j]:
                nums[k] = left[i]
                i += 1
            else:
                nums[k] = right[j]
                j +=1
            k +=1
        while i < len(left):
            nums[k] = left[i]
            i += 1
            k += 1
        while j < len(right):
            nums[k] = right[j]
            j += 1
            k += 1

list_1 = [1,5,6,2,3,7,2,1,55,1,2,2]
merge_sort(list_1)
print(list_1)
