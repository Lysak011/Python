# Задача 30:  Заполните массив элементами арифметической прогрессии.
# Её первый элемент, разность и количество элементов нужно ввести с клавиатуры.
# Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d.
# Каждое число вводится с новой строки.

# 1,2,3,4 (d=1)
# 3,5,7,9 (d=2)
# a = int(input("Введите первый элемент: "))
# d = int(input("Введите разность: "))
# n = int(input("Введите количество элементов: "))


import random
a = (random.randint(1, 5))
print(f'Первый элемент (a) = {a}')
d = (random.randint(1, 5))
print(f'Разность (d) = {d}')
n = (random.randint(3, 10))
print(f'Количество элементов (n) ={n}')

for i in range(n):
    print(a + i * d, end=' ')




