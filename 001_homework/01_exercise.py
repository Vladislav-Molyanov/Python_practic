#    1. Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным.
#Пример:
#        ◦ 6 -> да
#        ◦ 7 -> да
#        ◦ 1 -> нет
print('Введите день недели')
dayWeek = int(input())

def CheckingDayOfWeek (arg):
    Monday = 1
    Friday = 5
    for i in range(Monday, Friday +1):
        if(arg == i):
           return 'будни'
    if (arg == 6 or arg == 7):
        return'Выходной'
    else:
        return 'Такого дня недели нет'

print(CheckingDayOfWeek(dayWeek))