#    5. Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве.
#Пример:
#        ◦ A (3,6); B (2,1) -> 5,09
#        ◦ A (7,-5); B (1,-1) -> 7,21

print('Введите координаты точки А')
x1 = int(input())
y1 = int(input())

print('Введите координаты точки В')
x2 = int(input())
y2 = int(input())

import math

DifferenceSquared = math.sqrt((pow(x2 - x1,2) + pow(y2 - y1,2)))
print(DifferenceSquared)
