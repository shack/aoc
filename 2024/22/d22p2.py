import re
import math
from functools import reduce, cmp_to_key
from itertools import combinations, permutations, product
from collections import Counter, deque

def sim(x, n):
    def mix_prune(n, m):
        return (n ^ m) & 16777215
    res = [x % 10]
    for _ in range(n):
        x = mix_prune(x, x << 6)
        x = mix_prune(x, x >> 5)
        x = mix_prune(x, x << 11)
        res.append(x % 10)
    changes = [ a - b for a, b in zip(res[1:], res[:-1]) ]
    return res[4:], [ tuple(changes[i-4:i]) for i in range(len(changes) + 1) ][4:]

input = [ l.strip() for l in open(0) ]
prices = [ sim(int(n), 2000) for n in input ]
res = Counter()
for ps, cs in prices:
    assert len(ps) == len(cs)
    seen = set()
    for p, c in zip(ps, cs):
        if not c in seen:
            res[c] += p
            seen.add(c)
print(max(res.values()))