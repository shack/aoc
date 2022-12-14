def input(name='input.txt'):
    with open(name, 'rt') as f:
        for l in f:
            yield l.rstrip()

def score(a, b):
    a = ord(a) - ord('A')
    b = ord(b) - ord('X')
    return 1 + b + ((b - a + 1) % 3) * 3

def choose(a, b):
    a = ord(a) - ord('A')
    b = ord(b) - ord('X')
    c = (a + b - 1) % 3
    return c + 1 + b * 3

def p1():
    overall = 0
    for l in input():
        a, b = l.split()
        overall += score(a, b)
    print(overall)

def p2():
    overall = 0
    for l in input():
        a, b = l.split()
        overall += choose(a, b)
    print(overall)

p1()
p2()