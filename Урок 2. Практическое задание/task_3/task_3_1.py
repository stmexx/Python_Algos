"""
3.	Сформировать из введенного числа обратное по порядку входящих в него
цифр и вывести на экран. Например, если введено число 3486,
то надо вывести число 6843.

Подсказка:
Используйте арифм операции для формирования числа, обратного введенному

Пример:
Введите число: 123
Перевернутое число: 321

ЗДЕСЬ ДОЛЖНА БЫТЬ РЕАЛИЗАЦИЯ ЧЕРЕЗ ЦИКЛ
"""

n = int(input('Введите число: '))
m = 0
while n > 0:
    m = m * 10 + n % 10
    n = n // 10
print(f'Перевернутое число: {m}')

# Не вышло сделать что б при вводе 120 было 021,
# в теории через IF можно было б как то отсчитывать количество 0 и потом
# подставить в начало
