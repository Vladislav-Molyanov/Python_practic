'''Задайте числами список из N элементов, заполненных из промежутка [-N, N]. 
Найдите произведение элементов на указанных позициях. 
Позиции хранятся в файле file.txt в одной строке одно число.'''
result = 1
n = int(input('Введите число N: '))
my_list = [i for i in range(-n, n + 1)]
print(my_list)
with open('002_homework/file.txt', 'r') as my_file:
    for i in my_file.readlines():
       result *= my_list[int(i)] 

print(result)       