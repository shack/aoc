import re
import math
from functools import reduce, cmp_to_key
from itertools import combinations, permutations, product
from collections import Counter, deque

input = [ l.strip() for l in open(0) ]

def turn(l, n):
    assert len(l) >= n
    w = len(l) - (n - 1)
    p = l[:w]
    a = max(p)
    ai = p.index(a)
    return str(a) + (turn(l[ai+1:], n - 1) if n > 1 else '')

res = 0
for line in input:
    l = [ int(x) for x in line ]
    res += int(turn(l, 12))
print(res)

