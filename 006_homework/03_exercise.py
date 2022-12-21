'''Задача Измените код одной-двух решенных ранее задач (с прошлых семинаров или домашних работ), 
применив лямбды, filter, map, zip, enumerate, списочные выражения.'''

"""
Напишите программу, которая найдёт произведение пар чисел списка.
Парой считаем первый и последний элемент, второй и предпоследний и т.д.
Пример:
- [2, 3, 4, 5, 6] => [12, 15, 16];
- [2, 3, 5, 6] => [12, 15]
"""

my_list = [2, 3, 4, 5, 6]
print(list(map(lambda x: my_list[x] * my_list[-x - 1], range(int(len(my_list) / 2) + 1))))