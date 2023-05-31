"""
Даны три стороны треугольника a,b,c. Определите тип треугольника с заданными сторонами. Выведите одно из четырех слов:
rectangular для прямоугольного треугольника, acute для остроугольного треугольника, obtuse для тупоугольного
треугольника или impossible, если треугольника с такими сторонами не существует (считаем, что вырожденный
треугольник тоже невозможен).
"""

a, b, c = int(input()), int(input()), int(input())
h = max(a, b, c)
j = min(a, b, c)
k = (a + b + c) - (h + j)
if h**2 == j**2 + k**2 and (h < j + k) and (h > j - k):
    print('rectangular')
elif h**2 < j**2 + k**2 and (h < j + k) and (h > j - k):
    print('acute')
elif h**2 > j**2 + k**2 and (h < j + k) and (h > j - k):
    print('obtuse')
else:
    print('impossible')
