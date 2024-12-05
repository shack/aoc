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

r = 0
order = defaultdict(list)
for l in input:
    if '|' in l:
        a, b = l.split('|')
        order[a].append(b)
    if ',' in l:
        p = l.split(',')
        if correct(p, order):
            m = p[len(p)//2]
            print(p, m)
            r += int(m)
print(r)