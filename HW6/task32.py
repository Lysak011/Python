# Задача 32: Определить индексы элементов массива (списка),
# значения которых принадлежат заданному диапазону
# (т.е. не меньше заданного минимума и не больше заданного максимума)

import random
my_list = [random.randint(1, 100) for i in range(10)]
print(my_list)
min = (random.randint(1, 10))
max = (random.randint(1, 100))
print(f'Минимум - {min}')
print(f'Максмиум - {max}')


for i in range(len(my_list)):
    if min <= my_list[i] <= max:
        print(i, end=' ')


