import re
from functools import reduce, cmp_to_key
from collections import Counter

def next(m, x, y, px, py):
    if m[y][x] == '|':
        return (x, y + 1) if py == y - 1 else (x, y - 1)
    elif m[y][x] == '7':
        return (x, y + 1) if px == x - 1 else (x - 1, y)
    elif m[y][x] == 'F':
        return (x + 1, y) if py == y + 1 else (x, y + 1)
    elif m[y][x] == '-':
        return (x + 1, y) if px == x - 1 else (x - 1, y)
    elif m[y][x] == 'J':
        return (x - 1, y) if py == y - 1 else (x, y - 1)
    elif m[y][x] == 'L':
        return (x + 1, y) if py == y - 1 else (x, y - 1)
    else:
        assert False

visit = {}

def p1(input):
    for y, l in enumerate(input):
        if (x := l.find('S')) != -1:
            break
    visit[y] = set([x])
    sx, sy = x, y
    px, py = x, y
    r = input[y][x+1]
    d = input[y+1][x]
    if '-7J'.find(r) != -1:
        x = x + 1
    elif '|LJ'.find(d) != -1:
        y = y + 1
    cnt = 0
    while (x, y) != (sx, sy):
        if not y in visit:
            visit[y] = set()
        assert not x in visit[y]
        visit[y].add(x)
        nx, ny = next(input, x, y, px, py)
        px, py = x, y
        x, y = nx, ny
        cnt += 1
    assert cnt % 2 != 0
    print(cnt // 2 + 1)

def p2(input):
    inside = 0
    for y in sorted(visit.keys()):
        l = ''.join(input[y][x] if x in visit[y] else ' ' for x in range(len(input[y])))
        io = [ m.span() for m in re.finditer('(?:F-*J)|(?:L-*7)|(?:\|)', l) ]
        b = [ (r0, l1) for ((_, r0), (l1, _)) in zip(io[::2], io[1::2]) ]
        inside += sum(len(set(range(l, r)) - visit[y]) for l, r in b)
    print(inside)

input = [ l.strip() for l in open(0) ]

p1(input)
p2(input)