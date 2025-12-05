import re
import math
from functools import reduce, cmp_to_key
from itertools import combinations, permutations, product
from collections import Counter, deque

input = [ l.strip() for l in open(0) ]

intv = []

fresh = 0
for line in input:
    m = re.match(r'(\d+)-(\d+)', line)
    if m:
        a, b = map(int, m.groups())
        intv.append((a, b))
    elif line:
        v = int(line)
        for a, b in intv:
            if a <= v <= b:
                fresh += 1
                break
print(fresh)
