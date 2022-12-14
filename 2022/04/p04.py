def input(name='input.txt'):
    with open(name, 'rt') as f:
        for l in f:
            yield l.rstrip()

def coords(l):
    a, b = l.split(',')
    return map(int, a.split('-') + b.split('-'))

def p1():
    cnt = 0
    for l in input():
        a1, a2, b1, b2 = coords(l)
        if (a1 <= b1 <= b2 <= a2) or (b1 <= a1 <= a2 <= b2):
            cnt = cnt + 1
    print(cnt)

def p2():
    cnt = 0
    for l in input():
        a1, a2, b1, b2 = coords(l)
        if (a1 <= b1 <= a2) or (b1 <= a1 <= b2):
            cnt = cnt + 1
    print(cnt)

p1()
p2()