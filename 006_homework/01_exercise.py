'''1. Наибольший общий делитель
В модуле math есть функция math.gcd(a, b), возвращающая наибольший общий делитель (НОД) двух чисел. 
Вычислите и напечатайте наибольший общий делитель для списка натуральных чисел. 
Ввод чисел продолжается до ввода пустой строки.
Входные данные Выходные данные
36 6
12
144
18
'''

from math import gcd

my_list = []
numb = int(input('Введите число, если хотите остановить ввод чисел, то введите пустую строку: '))
my_list.append(numb)
while numb:
    numb = input('Введите число, если хотите остановить ввод чисел, то введите пустую строку: ')
    if numb:
        numb = int(numb)
        my_list.append(numb)
        print(my_list)
        for i in range(len(my_list) - 1):
            if i == 0:
                gcd_num = gcd(my_list[i], my_list[i + 1])
            else:
                gcd_num = gcd(gcd_num, my_list[i + 1])
        print(f'НОД {my_list} = {gcd_num}')