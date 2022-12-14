def input(name='input.txt'):
    with open(name, 'rt') as f:
        for l in f:
            yield l.rstrip()

def score(e):
    return ord(e) + (27 - ord('A') if e.isupper() else 1 - ord('a'))

def p1():
    s = 0
    for l in input():
        n = len(l) // 2
        a, b = l[:n], l[n:]
        e = (set(a) & set(b)).pop()
        s += score(e)
    print(s)

def n_elements(n: int, it):
    try:
        while True:
            yield [next(it) for j in range(0, n)]
    except StopIteration:
        return

def p2():
    s = 0
    for a, b, c in n_elements(3, input()):
        e = (set(a) & set(b) & set(c)).pop()
        s += score(e)
    print(s)

p1()
p2()