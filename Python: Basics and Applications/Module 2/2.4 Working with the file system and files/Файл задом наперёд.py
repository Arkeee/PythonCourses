"""
Вам дается текстовый файл, содержащий некоторое количество непустых строк.
На основе него сгенерируйте новый текстовый файл, содержащий те же строки в обратном порядке.

Пример входного файла:
ab
c
dde
ff

Пример выходного файла:
ff
dde
c
ab
"""


with open("tests files/test.txt") as infile:
    content = infile.read().splitlines()
    with open("tests files/new_file", "w") as outfile:
        outfile.write("\n".join(content[::-1]))
