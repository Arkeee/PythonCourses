"""Вам дана последовательность строк.
Выведите строки, содержащие обратный слеш "\"."""

import sys
import re


for line in sys.stdin:
    line = line.rstrip()
    result = re.search(r'\\', line)
    if result:
        print(line)
