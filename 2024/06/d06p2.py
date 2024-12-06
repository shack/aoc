import re
import math
from functools import reduce, cmp_to_key
from itertools import combinations, permutations, product
from collections import Counter, deque

input = [ list(l.strip()) for l in open(0) ]

def find_start():
    for y, l in enumerate(input):
        for x, c in enumerate(l):
            match c:
                case '<': return x, y, -1, 0
                case '>': return x, y, 1, 0
                case '^': return x, y, 0, -1
                case 'v': return x, y, 0, 1
                case _:
                    pass

def walk(x, y, dx, dy):
    pos = set()
    while True:
        pos.add((x, y, dx, dy))
        nx, ny = x + dx, y + dy
        if not (0 <= nx < N and 0 <= ny < N):
            return False
        if input[ny][nx] == '#':
            dx, dy = -dy, dx
        else:
            x, y = nx, ny
        if (x, y, dx, dy) in pos:
            return True

sx, sy, dx, dy = find_start()
N = len(input)
res = 0
for y, l in enumerate(input):
    for x, c in enumerate(l):
        if c != '.':
            continue
        input[y][x] = '#'
        if walk(sx, sy, dx, dy):
            res += 1
        input[y][x] = '.'
print(res)