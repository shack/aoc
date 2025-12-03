import re
import math
from functools import reduce, cmp_to_key
from itertools import combinations, permutations, product
from collections import Counter, deque

input = [ l.strip() for l in open(0) ]

res = 0
for line in input:
    l = [ int(x) for x in line ]
    a = max(l[:-1])
    ai = l.index(a)
    b = max(l)
    bi = l.index(b)
    if b > a:
        j = 10 * a + l[-1]
    else:
        j = 10 * a + max(l[ai+1:], default=0)
    res += j
print(res)

