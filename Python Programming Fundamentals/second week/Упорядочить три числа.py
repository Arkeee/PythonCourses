"""
Дано три числа. Упорядочите их в порядке неубывания. Программа должна считывать три числа a,b,c, затем программа должна
 менять их значения так, чтобы стали выполнены условия a≤b≤c, затем программа выводит тройку a,b,c.

Дополнительные ограничения: нельзя использовать дополнительные переменные.
"""

a, b, c = int(input()), int(input()), int(input())
a, b = max(a, b), min(a, b)
a, c = max(a, c), min(a, c)
b, c = max(b, c), min(b, c)
print(c, b, a)
