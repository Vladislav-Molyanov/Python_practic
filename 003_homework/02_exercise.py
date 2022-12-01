'''Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.

Пример:

- [2, 3, 4, 5, 6] => [12, 15, 16];
- [2, 3, 5, 6] => [12, 15]'''

my_list = [2, 4, 1, 6, 7, 9, 6]
print([my_list[i] * my_list[-i - 1] for i in range(int(len(my_list) / 2) + 1)])