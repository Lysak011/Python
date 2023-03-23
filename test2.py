
import random

N = int(input("Введите количество элементов в массиве "))
list = [random.randint(1, 5) for i in range(N)]
print(list)
x = int(input("Введите искомое число "))
index_num = 0
min_num = abs(x - list[0])
for i in range(1, N):
    buffer_num = abs(x -list[i])
    if buffer_num < min_num:
        min_num = buffer_num
        index_num = i

print(f"-> {list[index_num]}")