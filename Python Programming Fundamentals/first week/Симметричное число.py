"""
Дано четырехзначное число. Определите, является ли его десятичная запись симметричной. Если число симметричное, то
выведите 1, иначе выведите любое другое целое число. Число может иметь меньше четырех знаков, тогда нужно считать,
что его десятичная запись дополняется слева нулями.
"""

a = int(input())
n1 = a - (a // 10) * 10
n2 = (a - (a // 100) * 100) // 10
n3 = (a - (a // 1000) * 1000) // 100
n4 = a // 1000
print(int(str(n3) + str(n4)) - int(str(n2) + str(n1)) + 1)
