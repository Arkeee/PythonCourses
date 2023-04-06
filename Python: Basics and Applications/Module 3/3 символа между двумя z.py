import re


words = [input() for _ in range(6)]
for word in words:
    result = re.search(r'z.{3}z', word)
    if result:
        print(word)
