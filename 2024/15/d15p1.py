import re
import math
from functools import reduce, cmp_to_key
from itertools import combinations, permutations, product
from collections import Counter, deque

input = open(0).read()
m, cmd = input.split('\n\n')
cmd = cmd.replace('\n', '')
m = [ list(l) for l in m.split('\n') ]

for y, l in enumerate(m):
    for x, c in enumerate(l):
        if c == '@':
            break
    else:
        continue
    break

def move(x, y, dx, dy):
    nx, ny = x + dx, y + dy
    if m[ny][nx] == 'O':
        move(nx, ny, dx, dy)
    if m[ny][nx] == '.':
        m[ny][nx] = m[y][x]
        m[y][x] = '.'
        x, y = nx, ny
    return x, y

for c in cmd:
    assert m[y][x] == '@'
    match c:
        case '>': dx, dy = 1, 0
        case '<': dx, dy = -1, 0
        case '^': dx, dy = 0, -1
        case 'v': dx, dy = 0, 1
    x, y = move(x, y, dx, dy)

res = 0
for y, l in enumerate(m):
    for x, c in enumerate(l):
        if c == 'O':
            res += 100 * y + x
print(res)

