"""Пирожок в столовой стоит A рублей и B копеек. Определите, сколько рублей и копеек нужно заплатить за N пирожков.

Формат ввода

Программа получает на вход три числа: A, B, N —  целые, неотрицательные, не превышают 10000.

Формат вывода

Программа должна вывести два числа: стоимость покупки в рублях и копейках."""

a, b, n = int(input()), int(input()), int(input())
print((a * n + b * n // 100), b * n % 100)
