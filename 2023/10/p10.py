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

sx, sy = 0, 0

def p1(input):
    for y, l in enumerate(input):
        if (x := l.find('S')) != -1:
            break
    visit[y].add(x)
    sx, sy = x, y
    px, py = sx, sy
    n = input[y-1][x] if y > 0 else '.'
    e = input[y][x+1] if x < len(input[y]) - 1 else '.'
    s = input[y+1][x] if y < len(input) - 1 else '.'
    w = input[y][x-1] if x > 0 else '.'
    na = n in '|F7'
    ea = e in '-J7'
    sa = s in '|JL'
    wa = w in '-LF'
    if na and ea:
        x = x + 1
        S = 'L'
    elif na and sa:
        y = y + 1
        S = '|'
    elif na and wa:
        x = x - 1
        S = 'J'
    elif ea and sa:
        y = y + 1
        S = 'F'
    elif ea and wa:
        x = x + 1
        S = '-'
    elif sa and wa:
        y = y + 1
        S = '7'
    input[sy] = input[sy].replace('S', S)
    cnt = 0
    while (x, y) != (sx, sy):
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
    for v, m in zip(visit, input):
        l = ''.join(m[x] if x in v else ' ' for x in range(len(m)))
        io = [ m.span() for m in re.finditer('(F-*J)|(L-*7)|(\|)', l) ]
        b = [ (r0, l1) for ((_, r0), (l1, _)) in zip(io[::2], io[1::2]) ]
        inside += sum(len(set(range(l, r)) - v) for l, r in b)
    print(inside)

input = [ l.strip() for l in open(0) ]
visit = [ set() for _ in input ]

p1(input)
p2(input)