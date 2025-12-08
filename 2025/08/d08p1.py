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

closest = sorted(combinations(input, 2), key=lambda x: dist(x[0], x[1]))

for a, b in closest[:1000]:
    uf[find(b)] = find(a)

sets = defaultdict(set)
for p in uf:
    sets[find(p)].add(p)

l = list(reversed(sorted([ len(s) for s in sets.values() ])))
print(l[0] * l[1] * l[2])




