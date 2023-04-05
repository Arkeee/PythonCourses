"""
В первой строке дано три числа, соответствующие некоторой дате date -- год, месяц и день.
Во второй строке дано одно число days -- число дней.

Вычислите и выведите год, месяц и день даты, которая наступит, когда с момента исходной даты date пройдет число дней,
равное days.

Примечание:
Для решения этой задачи используйте стандартный модуль datetime.
Вам будут полезны класс datetime.date для хранения даты и класс datetime.timedelta﻿ для прибавления дней к дате.
"""

from datetime import date, timedelta


old_date = list(map(int, input().split()))
new_date = date(old_date[0], old_date[1], old_date[2]) + timedelta(days=int(input()))
print(new_date.year, new_date.month, new_date.day)
