import re


words = [input() for _ in range(2)]
for word in words:
    result = re.search(r'\\', word)
    if result:
        print(word)