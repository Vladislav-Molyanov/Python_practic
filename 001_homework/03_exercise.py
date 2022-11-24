#    3. Напишите программу, которая принимает на вход координаты точки (X и Y), причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости, в которой находится эта точка (или на какой оси она находится).
#Пример:
#        ◦ x=34; y=-30 -> 4
#        ◦ x=2; y=4-> 1
#        ◦ x=-34; y=-30 -> 3

print('Введите точку X')
numX = int(input())

print('Введите точку Y')
numY = int(input())

def CoordinateCheck (pointX,pointY):
    if (pointX < 0 and pointY > 0):
        return 'Первая четверть'
    elif (pointX > 0 and pointY > 0):
        return 'Вторая четверть'
    elif (pointX < 0 and pointY < 0):
        return 'Третья четверть'
    elif (pointX > 0 and pointY < 0):
        return 'Четвертая четверть'

print(CoordinateCheck(numX,numY))