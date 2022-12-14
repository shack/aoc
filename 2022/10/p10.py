def input(name='input.txt'):
    with open(name, 'rt') as f:
        for l in f:
            yield l.rstrip()

def simulate(f):
    x = 1
    c = 1
    v = 0
    state = 0
    inp = input()
    try:
        while True:
            f(c, x)
            if state == 0:
                l = next(inp)
                l = l.split()
                if l[0] == 'noop':
                    state = 3
                    pass
                elif l[0] == 'addx':
                    state = 2
                    v = int(l[1])
            if state == 3:
                c += 1
                state = 0
            elif state == 2:
                c+= 1
                state = 1
            elif state == 1:
                c+= 1
                x += v
                state = 0
    except:
        pass

def p1():
    cycles = set([20, 60, 100, 140, 180, 220])
    s = 0
    def strength(c, x):
        nonlocal s
        if c in cycles:
            s += c * x
    simulate(strength)
    print(s)

def p2():
    def plot(c, x):
        h = (c - 1) % 40
        print('#' if h == x - 1 or h == x or h == x + 1 else '.', end='')
        if h == 39:
            print('')
    simulate(plot)

p1()
p2()