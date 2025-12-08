import re
import math
from functools import reduce, cmp_to_key
from itertools import combinations, permutations, product
from collections import Counter, deque, defaultdict

input = [ l.strip() for l in open(0) ]
input = [ tuple(map(int, l.split(','))) for l in input ]

def dist(a, b):
    a0, a1, a2 = a
    b0, b1, b2 = b
    dx, dy, dz = a0 - b0, a1 - b1, a2 - b2
    return math.sqrt(dx * dx + dy * dy + dz * dz)

uf = { p: p for p in input }

def find(p):
    return p if p == uf[p] else find(uf[p])

closest = sorted([ (a, b, dist(a, b)) for a, b in combinations(input, 2) ], key=lambda x: x[2])

for i, (a, b, d) in enumerate(closest):
    uf[find(b)] = find(a)
    curr = find(b)
    for p in uf:
        if find(p) != curr:
            break
    else:
        print(a[0] * b[0])
        break