"""Вам дана частичная выборка из датасета зафиксированных преступлений, совершенных в городе Чикаго с 2001
года по настоящее время.

Одним из атрибутов преступления является его тип – Primary Type.

Вам необходимо узнать тип преступления, которое было зафиксировано максимальное число раз в 2015 году."""

import csv

primary = {}
with open('Crimes.csv') as f:
    reader = csv.reader(f)
    for row in reader:
        primary[row[5]] = primary.get(row[5], 0) + 1
print({x: y for x, y in filter(lambda x: primary[x[0]] == max(primary.values()), primary.items())})
