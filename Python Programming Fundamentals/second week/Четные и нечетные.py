"""
Даны три целых числа A, B, C. Определить, есть ли среди них хотя бы одно четное и хотя бы одно нечетное.
"""

a, b, c = int(input()), int(input()), int(input())
if a % 2 == b % 2 == c % 2:
    print('NO')
else:
    print('YES')
