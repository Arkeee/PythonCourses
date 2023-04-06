"""Вам дана последовательность строк.В каждой строке замените первое вхождение слова, состоящего
только из латинских букв "a" (регистр не важен), на слово "argh"."""

import re


words = [input() for _ in range(2)]
for line in words:
    print(re.sub(r'\b(A|a)+\b', 'argh', line, count=1))

