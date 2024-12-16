import re
import math
from functools import reduce, cmp_to_key
from itertools import combinations, permutations, product
from collections import Counter, deque
import sys
sys.setrecursionlimit(50000)

input = [ l.strip() for l in open(0) ]

for cy, l in enumerate(input):
    for cx, c in enumerate(l):
        match c:
            case 'S':
                sx, sy = cx, cy
            case 'E':
                ex, ey = cx, cy

def rotate_ccw(dx, dy):
    return -dy, dx

best = set()

def search(x, y, dx, dy, score, visited, path, best):
    if (x, y, dx, dy) in visited and score > visited[(x, y, dx, dy)]:
        return visited[(x, y, dx, dy)]
    visited[(x, y, dx, dy)] = score
    path.append((x, y))
    if (x, y) == (ex, ey):
        print('!', score)
        best.add((score, tuple(path)))
    costs = []
    for sc in [0, 1000, 2000, 1000]:
        if input[y + dy][x + dx] != '#':
            a = search(x + dx, y + dy, dx, dy, sc + score + 1, visited, path, best)
            costs.append(a)
        dx, dy = rotate_ccw(dx, dy)
    path.pop()
    return min(costs) if costs else 1000000000000

best = set()
search(sx, sy, 1, 0, 0, {}, [], best)

m = min(s for s, _ in best)
print(m)
res = set()
for s, p in best:
    if s == m:
        res |= set(p)
print(len(res))


