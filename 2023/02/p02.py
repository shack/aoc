import re
from functools import reduce

def p1():
    f = open('input.txt', 'r')
    possibles = {
        'red': 12,
        'green': 13,
        'blue': 14,
    }
    sum = 0
    for i, l in enumerate(f):
        if all(int(n) <= possibles[col] for n, col in re.findall(r'(\d+) (\w+)', l)):
            sum += i + 1
    print(sum)

def p2():
    f = open('input.txt', 'r')
    sum = 0
    for l in f:
        maxs = { }
        for n, col in re.findall(r'(\d+) (\w+)', l):
            maxs[col] = max(maxs.get(col, 0), int(n))
        sum += reduce(lambda x, y: x * y, maxs.values())
    print(sum)

p1()
p2()


