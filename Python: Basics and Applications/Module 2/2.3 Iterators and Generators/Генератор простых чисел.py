import itertools


def primes():
    a = 1
    numbers = []
    while True:
        a += 1
        for i in numbers:
            if a % i == 0:
                break
        else:
            numbers.append(a)
            yield a


print(list(itertools.takewhile(lambda x: x <= 31, primes())))
