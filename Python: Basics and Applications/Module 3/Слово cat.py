import re

lines = [input() for _ in range(7)]
for line in lines:
    line = line.rstrip()
    result = re.findall(r'\bcat\b', line)
    if result:
        print(line)
