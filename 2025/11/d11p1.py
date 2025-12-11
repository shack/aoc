import re
import math
from functools import reduce, cmp_to_key
from itertools import combinations, permutations, product
from collections import Counter, deque, defaultdict

input = [ l.strip() for l in open(0) ]

g = defaultdict(set)

for l in input:
    n, r = l.split(':')
    for d in r.split():
        g[n.strip()].add(d.strip())

res = {}
def search(v):
    if v == 'out':
        return 1
    r = 0
    for n in g[v]:
        if n in res:
            r += res[n]
        else:
            r += search(n)
    res[v] = r
    return r

print(search('you'))




