import re
import math
from functools import reduce, cmp_to_key, cache
from itertools import combinations, permutations, product
from collections import Counter, deque, defaultdict

input = [ l.strip() for l in open(0) ]

g = defaultdict(set)

for l in input:
    n, r = l.split(':')
    for d in r.split():
        g[n.strip()].add(d.strip())

@cache
def search(v):
    if v == 'out':
        return 1
    return sum(search(n) for n in g[v])

print(search('you'))




