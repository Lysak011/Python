#Дана последовательность из N целых чисел и число K.
# Необходимо сдвинуть всю последовательность (сдвиг - циклический) на K элементов вправо, K – положительное число.

import random

n = int(input("введите N - длинна последовательности: "))
k = int(input("Введите к - сдвиг последовательности"))

numb_list = [i for i in range(n)]
test_list = numb_list[len(numb_list) - k:]
test_list2 = numb_list[k:len(numb_list) - k]
print(numb_list)
print(test_list)
print(test_list2)
numb_list = test_list + test_list2
print(numb_list)

# for i in range (len(numb_list)):
#     numb_list[i] , numb_list[]

a = [1, 2, 3, 4, 5]
b = [6, 7, 8, 9]
# print(a[1:-2])

