'''Реализуйте алгоритм перемешивания списка 
(shuffle использовать нельзя, другие методы из библиотеки random - можно).'''

import random as rnd


def my_shuffle(arg: list) -> list:
    arr = arg.copy()
    arg.clear()
    while len(arr) != len(arg):
        elem = rnd.choice(arr)
        if arg.count(elem) != arr.count(elem):
            arg.append(elem)

my_list = [1,2,3,4,5,6,7,8,9]
print(my_list)
my_shuffle(my_list)
print(my_list)