'''Задайте натуральное число N. Напишите программу,
которая составит список простых множителей числа N.'''

def primfacs(n):
    i = 2
    primfac = []
    while i * i <= n:
        while not n % i:
            primfac.append(i)
            n /= i
        i += 1
    if n > 1:
        primfac.append(int(n))
    return primfac

n = int(input('Введите число: '))
print(primfacs(n))