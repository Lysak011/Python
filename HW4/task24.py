# Задача 24: В фермерском хозяйстве в Карелии выращивают чернику. Она растет на круглой грядке, причем кусты высажены только по окружности.
# Таким образом, у каждого куста есть ровно два соседних. Всего на грядке растет N кустов.
# Эти кусты обладают разной урожайностью, поэтому ко времени сбора на них выросло различное число ягод – на i-ом кусте выросло ai ягод.
# В этом фермерском хозяйстве внедрена система автоматического сбора черники. Эта система состоит из управляющего модуля и нескольких собирающих модулей.
# Собирающий модуль за один заход, находясь непосредственно перед некоторым кустом, собирает ягоды с этого куста и с двух соседних с ним.
# Напишите программу для нахождения максимального числа ягод, которое может собрать за один заход собирающий модуль, находясь перед некоторым кустом заданной во входном файле грядки.

import random

garden = list(random.randint(0, 10) for i in range(random.randint(3, 10)))
print("Наша грядка состоит из", len(garden), "таких кустов:", garden)
bush = int(random.randint(1, len(garden)))
print('Собираем ягоды с', bush, 'куста и двух соседних.')
berry = 0
if bush == 1:
    berry = garden[0] + garden[1] + garden[-1]
elif bush == len(garden):
    berry = garden[-2] + garden[-1] + garden[0]
else:
    berry = garden[bush-1] + garden[bush-2] + garden[bush]
print('Итого:',berry, 'ягод, с трех кустов.')