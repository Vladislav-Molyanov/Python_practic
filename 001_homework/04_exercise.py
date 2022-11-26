# Напишите программу, которая по заданному номеру четверти, 
# показывает диапазон возможных координат точек в этой четверти (x и y).
print('Введите номер четверти')

QuarterNumber = int(input())
if(QuarterNumber == 1):
    print('(x>0,y>0)')
elif(QuarterNumber == 2):
    print('(x<0,y>0)')
elif(QuarterNumber == 3):
    print('(x<0,y<0)')
elif(QuarterNumber == 4):
    print('(x>0,y<0)')
