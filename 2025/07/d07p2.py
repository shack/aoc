import re
import math
from functools import reduce, cmp_to_key
from itertools import combinations, permutations, product
from collections import Counter, deque

input = [ l.strip() for l in open(0) ]

sx, sy = 0, 0
for y, r in enumerate(input):
    for x, c in enumerate(r):
        if c == 'S':
            sx, sy = x, y

x_active = Counter()
x_active[sx] = 1

for y, r in enumerate(input):
    start = 0
    next_act = Counter()
    while True:
        idx = r.find('^', start)
        if idx == -1:
            break
        else:
            start = idx + 1
            if idx in x_active:
                next_act[idx - 1] += x_active[idx]
                next_act[idx + 1] += x_active[idx]
                x_active[idx] = 0
    x_active.update(next_act)
print(sum(x_active.values()))