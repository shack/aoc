import re

p = re.compile(r'move (\d+) from (\d+) to (\d+)')

def input(name='input.txt'):
    with open(name, 'rt') as f:
        for l in f:
            yield l.rstrip()

def p1():
    index = 0
    crates = [ list() for i in range(0, 9) ]
    inp = input()
    for l in inp:
        pos = 0
        while True: 
            pos = l.find('[', pos)
            if pos == -1:
                break
            stack = pos // 4
            pos = pos + 1
            crate = l[pos]
            assert stack < len(crates)
            crates[stack].append(crate)
        match = p.findall(l)
        if len(match) == 3:
            n, f, t = map(int, match[0])
            f = f - 1
            t = t - 1
            for i in range(0, n):
                e = crates[f][0]
                crates[f] = crates[f][1:]
                crates[t] = [e] + crates[t]
    print(''.join([s[0] for s in crates ]))

def p2():
    index = 0
    crates = [ list() for i in range(0, 9) ]
    for l in input():
        match = p.findall(l)
        if len(match) > 0:
            n, f, t = match[0]
            n, f, t = map(int, [n, f, t])
            f = f - 1
            t = t - 1
            e = crates[f][0:n]
            crates[f] = crates[f][n:]
            crates[t] = e + crates[t]
        pos = 0
        while True: 
            pos = l.find('[', pos)
            if pos == -1:
                break
            stack = pos // 4
            pos = pos + 1
            crate = l[pos]
            assert stack < len(crates)
            crates[stack].append(crate)
    print(''.join([s[0] for s in crates ]))

p1()
p2()