"""Вам дана последовательность строк.
Выведите строки, содержащие "cat" в качестве подстроки хотя бы два раза.

Примечание:
Считать все строки по одной из стандартного потока ввода вы можете, например, так

import sys

for line in sys.stdin:
    line = line.rstrip()
    # process line"""

import sys
import re


for line in sys.stdin:
    line = line.rstrip()
    result = re.findall(r'cat.*cat', line)
    if result:
        print(line)
