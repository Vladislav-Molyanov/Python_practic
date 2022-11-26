#    1. Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным.
#Пример:
#        ◦ 6 -> да
#        ◦ 7 -> да
#        ◦ 1 -> нет
print('Введите день недели')
dayWeek = int(input())

def CheckingDayOfWeek (day):
    if day in range (1,6):
        return 'Да'
    elif day in (6,7):
        return 'Нет'
    else:
        return 'Такого дня недели нет'
print(CheckingDayOfWeek(dayWeek))