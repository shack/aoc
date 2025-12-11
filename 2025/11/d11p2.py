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

def search(v, tgt, forbid, res):
    if v == tgt:
        return 1
    elif v == forbid:
        return 0
    r = 0
    for n in g[v]:
        if n in res:
            r += res[n]
        else:
            r += search(n, tgt, forbid, res)
    res[v] = r
    return r

sd = search('svr', 'dac', 'fft', {})
sf = search('svr', 'fft', 'dac', {})
fd = search('fft', 'dac', '', {})
df = search('dac', 'fft', '', {})
fo = search('fft', 'out', 'dac', {})
do = search('dac', 'out', 'fft', {})

print(sd * df * fo + sf * fd * do)