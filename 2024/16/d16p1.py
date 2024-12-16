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

def search(x, y, dx, dy, score, visited):
    if (x, y, dx, dy) in visited and score > visited[(x, y, dx, dy)]:
        return visited[(x, y, dx, dy)]
    visited[(x, y, dx, dy)] = score
    costs = []
    for sc in [0, 1000, 2000, 1000]:
        if input[y + dy][x + dx] != '#':
            a = search(x + dx, y + dy, dx, dy, sc + score + 1, visited)
            costs.append(a)
        dx, dy = rotate_ccw(dx, dy)
    return min(costs) if costs else 1000000000000

print(sx, sy, ex, ey)
res = {}
search(sx, sy, 1, 0, 0, res)
print(res[(ex, ey)])


