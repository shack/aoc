import re
import math
from functools import reduce, cmp_to_key
from itertools import combinations, permutations, product
from collections import Counter, deque

input = [ l.strip() for l in open(0) ]

intv = []

for line in input:
    m = re.match(r'(\d+)-(\d+)', line)
    if m:
        a, b = map(int, m.groups())
        intv.append((a, b))
    elif not line:
        break

intv = sorted(intv, key=lambda x: x[0])
union = [ intv[0] ]
for s, e in intv[1:]:
    ls, le = union[-1]
    if s <= le:
        union[-1] = (ls, max(le, e))
    else:
        union.append((s, e))

res = 0
for a, b in union:
    res += b - a + 1
print(res)
