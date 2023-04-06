"""Вам дана последовательность строк.
Выведите строки, содержащие "cat" в качестве слова."""

import sys
import re


for line in sys.stdin:
    line = line.rstrip()
    result = re.findall(r'\bcat\b', line)
    if result:
        print(line)
