import re

numbers = [input() for _ in range(1)]
for number in numbers:
    number = re.sub(r'\D', r' ', number)
    try:
        if int(number, 2) % 3 == 0:
            print(number.replace(' ', ''))
    except ValueError:
        pass
