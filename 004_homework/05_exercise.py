'''Даны два файла, в каждом из которых находится запись многочлена. 
Задача - сформировать файл, содержащий сумму многочленов.
'''

with open('result.txt', 'r') as input_1, open('result2.txt', 'r') as input_2, open('total_result.txt', 'w') as output_f:
    polynomial_1 = input_1.read()[:-4].split(' + ')
    polynomial_2 = input_2.read()[:-4].split(' + ')
    polynomial_result = []
    if len(polynomial_1) < len(polynomial_2):
        for i in range(len(polynomial_2) - len(polynomial_1)):
            polynomial_1.insert(i, '0' + polynomial_2[i][-4:])
    else:
        for i in range(len(polynomial_1) - len(polynomial_2)):
            polynomial_2.insert(i, '0' + polynomial_1[i][-4:])
    for i, j in zip(polynomial_1, polynomial_2):
        if 'x' in i:
            polynomial_result.append(f'{int(i[:-4]) + int(j[:-4])}{i[-4:]}')
        else:
            polynomial_result.append(f'{int(i) + int(j)}')
    result = ' + '.join(polynomial_result) + ' = 0'
    output_f.write(result)