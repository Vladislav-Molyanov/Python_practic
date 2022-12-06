'''Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.

Пример:

- для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21] '''

def negaF(arg):
    if arg == -1:
        return 1
    elif arg == -2:
        return -1
    else:
        return negaF(arg + 2) - negaF(arg + 1)

def Fib(arg):
    if arg == 0:
        return 0
    elif arg == 1 :
        return 1
    else:
        return Fib(arg - 1) + Fib(arg - 2)

k = int(input('Введите число: '))
my_list = [negaF(i) for i in range(-k, 0)] + [Fib(i) for i in range(0, k + 1)]
print(my_list)