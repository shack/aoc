import re
import math
import copy
from functools import reduce, cmp_to_key
from itertools import combinations, permutations, product
from collections import Counter, deque

input = open(0).read()
m, cmd = input.split('\n\n')
cmd = cmd.replace('\n', '')

m = [ list(l.replace('#', '##').replace('.', '..').replace('O', '[]').replace('@', '@.')) for l in m.split('\n') ]

for y, l in enumerate(m):
    for x, c in enumerate(l):
        if c == '@':
            break
    else:
        continue
    break

def move(d, x, y):
    match d:
        case '>': dx, dy = 1, 0
        case '<': dx, dy = -1, 0
        case '^': dx, dy = 0, -1
        case 'v': dx, dy = 0, 1
    nx, ny = x + dx, y + dy
    if m[ny][nx] in '[]':
        if d in '<>':
            r, _ = move(d, nx, ny)
        else:
            if m[ny][nx] == '[':
                r, _ = move(d, nx + 1, ny)
            else:
                r, _ = move(d, nx - 1, ny)
            if r:
                r, _ = move(d, nx, ny)
    else:
        r = m[ny][nx] != '#'
    if r:
        assert m[ny][nx] == '.'
        m[ny][nx] = m[y][x]
        m[y][x] = '.'
        x, y = nx, ny
    return r, (x, y)

for d in cmd:
    assert m[y][x] == '@'
    backup = copy.deepcopy(m)
    r, (nx, ny) = move(d, x, y)
    if r:
        x, y = nx, ny
    else:
        m = backup

res = 0
for y, l in enumerate(m):
    for x, c in enumerate(l):
        if c == '[':
            res += 100 * y + x
print(res)

