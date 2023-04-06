import re


words = [input() for _ in range(4)]
for line in words:
    result = re.search(r'\b(\w+)\1\b', line)
    if result:
        print(line)