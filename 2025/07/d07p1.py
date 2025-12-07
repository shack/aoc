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

x_active = set()
x_active.add(sx)

n_split = 0
for y, r in enumerate(input):
    start = 0
    next_act = set()
    while True:
        idx = r.find('^', start)
        if idx == -1:
            break
        else:
            start = idx + 1
            if idx in x_active:
                x_active.remove(idx)
                next_act.add(idx - 1)
                next_act.add(idx + 1)
                n_split += 1
    x_active = x_active | next_act
print(n_split)