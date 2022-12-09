'''Задана натуральная степень k. Сформировать случайным образом список коэффициентов 
(значения от 0 до 100) многочлена и записать в файл многочлен степени k.

Пример:
k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0
'''
import random as rnd

k = int(input('Введите степень многочлена: '))
polinomial = []
for i in range(k - 1, -1, -1):
    coeff = rnd.randint(0, 100)
    if coeff != 0:
        if i != 0:
            polinomial.append(f'{coeff}*x^{i}')
        else:
            polinomial.append(f'{coeff}')
result = ' + '.join(polinomial) + ' = 0'
with open('result.txt', 'w') as output_f:
    output_f.write(result)