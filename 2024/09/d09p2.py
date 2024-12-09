import re
import math
import sys
from functools import reduce, cmp_to_key
from itertools import combinations, permutations, product
from collections import Counter, deque

input = [ l.strip() for l in open(0) ][0]
map = []

occ = [ (1, int(c)) for c in input[0::2] ]
free = [ int(c) for c in input[1::2] ]

alloc = [ list() for _ in free ]

f = 0
o = len(occ) - 1
end = 0
while o >= 0:
    act, sz = occ[o]
    for f, s in enumerate(free[0:o]):
        if s >= sz:
            free[f] -= sz
            alloc[f].append((o, sz))
            occ[o] = (0, sz)
            break
    o -= 1

map = []
for i, ((act, sz), f) in enumerate(zip(occ, free)):
    map += [i if act else 0] * int(sz)
    added = 0
    for id, sz in alloc[i]:
        map += [id] * sz
        added += sz
    for i in range(f):
        map.append(0)
print(sum(i * a for i, a in enumerate(map)))