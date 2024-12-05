import re
import math
from functools import reduce, cmp_to_key
from itertools import combinations, permutations, product
from collections import Counter, deque, defaultdict

input = [ l.strip() for l in open(0) ]

def correct(upd, order):
    for i, x in enumerate(upd):
        if not x in order:
            continue
        later = order[x]
        for y in upd[i+1:]:
            if not y in later:
                return False
            if x in order[y]:
                return False
    return True

def mycmp(x, y):
    if y in order[x]:
        return -1
    elif x in order[y]:
        return 1
    else:
        assert False
        return 0

r = 0
ps = []
order = defaultdict(list)
for l in input:
    if '|' in l:
        a, b = l.split('|')
        order[a].append(b)
    if ',' in l:
        p = l.split(',')
        ps.append(p)

for p in ps:
    if not correct(p, order):
        p = sorted(p, key=cmp_to_key(mycmp))
        m = p[len(p)//2]
        r += int(m)
print(r)