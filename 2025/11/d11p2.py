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
def search(v, tgt, forbid):
    if v == tgt:
        return 1
    elif v == forbid:
        return 0
    return sum(search(n, tgt, forbid) for n in g[v])

sd = search('svr', 'dac', 'fft')
sf = search('svr', 'fft', 'dac')
fd = search('fft', 'dac', '')
df = search('dac', 'fft', '')
fo = search('fft', 'out', 'dac')
do = search('dac', 'out', 'fft')

print(sd * df * fo + sf * fd * do)