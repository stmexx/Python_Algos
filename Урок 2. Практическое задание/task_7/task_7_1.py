"""
7.	Напишите программу, доказывающую или проверяющую, что для множества
натуральных чисел выполняется равенство: 1+2+...+n = n(n+1)/2,
где n - любое натуральное число.

ЗДЕСЬ ДОЛЖНА БЫТЬ РЕАЛИЗАЦИЯ ЧЕРЕЗ ЦИКЛ
"""
n = int(input('Введите любое натуральное число: '))
s = 0
for i in range(1, n + 1):
    s += i
m = n * (n + 1) // 2
print(f'Левая сторона равенства = {s}')
print(f'Правая сторона равенства = {m}')
if s == m:
    print('ОНИ РАВНЫЫЫЫ')