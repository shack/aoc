import re
import math
from functools import reduce, cmp_to_key
from itertools import combinations, permutations, product
from collections import Counter, deque

input = [ l.strip() for l in open(0) ]
Y = len(input)
X = len(input[0])

def expand_region(c, x, y):
    def exp(x, y):
        pts.add((x, y))
        for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            nx, ny = x + dx, y + dy
            if nx < 0 or nx >= X or ny < 0 or ny >= Y:
                continue
            if input[ny][nx] == c and not (nx, ny) in pts:
                exp(nx, ny)
    pts = set()
    exp(x, y)
    return pts

def circumference(r):
    res = 0
    for x, y in r:
        for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            nx, ny = x + dx, y + dy
            if not (nx, ny) in r:
                res += 1
    return res

all_seen = set()

res = 0
for y in range(Y):
    for x in range(X):
        c = input[y][x]
        if not (x, y) in all_seen:
            r = expand_region(c, x, y)
            all_seen |= r
            res += len(r) * circumference(r)
print(res)