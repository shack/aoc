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
        possible = True
        l = l.strip()
        _, rest = l.split(':')
        reveal = rest.split(';')
        for s in reveal:
            cubes = s.split(',')
            for p in cubes:
                n, col = p.strip().split(' ')
                possible &= int(n) <= possibles[col]
        if possible:
            sum += i + 1
    print(sum)



def p2():
    f = open('input.txt', 'r')
    sum = 0
    for l in f:
        maxs = {
            'red': 0,
            'green': 0,
            'blue': 0,
        }
        l = l.strip()
        _, rest = l.split(':')
        reveal = rest.split(';')
        for s in reveal:
            cubes = s.strip().split(',')
            for p in cubes:
                n, col = p.strip().split(' ')
                maxs[col] = max(maxs[col], int(n))
        sum += reduce(lambda x, y: x * y, maxs.values())
    print(sum)

p1()
p2()


