def input(name):
    with open(name, 'rt') as f:
        for l in f:
            yield l.rstrip()


def p1():
    cals = 0
    max_cals = 0
    for s in input('p01.txt'):
        try:
            cals += int(s)
        except:
            max_cals = max(max_cals, cals)
            cals = 0
    print(max_cals)

def p2():
    cals = 0
    all = []
    for s in input('p01.txt'):
        try:
            cals += int(s)
        except:
            all += [cals]
            cals = 0
    all.sort()
    print(sum(all[-3:]))

p1()
p2()