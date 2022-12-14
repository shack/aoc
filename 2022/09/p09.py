def input(name='input.txt'):
    with open(name, 'rt') as f:
        for l in f:
            yield l.rstrip()

def p2(n = 10):
    x = [0] * n
    y = [0] * n
    tail_positions = set()
    tail_positions.add((0, 0))
    for l in input():
        d, s = l.split(' ')
        s = int(s)
        for i in range(0, s):
            if d == 'U':
                y[0] = y[0] + 1
            elif d == 'D':
                y[0] = y[0] - 1
            elif d == 'L':
                x[0] = x[0] - 1
            else:
                x[0] = x[0] + 1
            for i in range(1, len(x)):
                dx = x[i-1] - x[i]
                dy = y[i-1] - y[i]
                if abs(dx) > 1 or abs(dy) > 1:
                    if dx == 0:
                        y[i] += dy // 2
                    elif dy == 0:
                        x[i] += dx // 2
                    else:
                        x[i] += 1 if dx > 0 else - 1
                        y[i] += 1 if dy > 0 else - 1
            tail_positions.add((x[-1], y[-1]))
    print(len(tail_positions))
    pass

def p1():
    p2(2)

p1()
p2()