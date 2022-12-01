"""    2. Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
Пример:
        ◦ пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 12, 123, 1234)"""
result = []
for i in range(1,int(input('Введите число N: ')) + 1):
    if not result:
        result.append(i)
    else:
        result.append(result[-1] * i)

print(result)
