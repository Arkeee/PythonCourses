"""Вам дана последовательность строк.
Выведите строки, содержащие слово, состоящее из двух одинаковых частей (тандемный повтор)."""

import sys
import re


for line in sys.stdin:
    line = line.rstrip()
    result = re.search(r'\b(\w+)\1\b', line)
    if result:
        print(line)
