# Задача 22: Даны два неупорядоченных набора целых чисел (может быть, с повторениями).
# Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
# Пользователь вводит 2 числа.
# n - кол-во элементов первого множества.
# m - кол-во элементов второго множества.
# Затем пользователь вводит сами элементы множеств.

import random

numb_list1 = [random.randint(0, 20) for _ in range(15)]
print(numb_list1)
numb_list2 = [random.randint(0, 20) for _ in range(15)]
print(numb_list2)
numb_list3 = []
# numb_list3 = set(numb_list1) & set(numb_list2)
# print(numb_list3)

for i in numb_list1:
    if i in numb_list3:
        continue
    for j in numb_list2:
        if i==j:
            numb_list3.append(i)
            break

print(sorted(numb_list3))