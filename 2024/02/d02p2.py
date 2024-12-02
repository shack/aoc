import re
import math
from functools import reduce, cmp_to_key
from itertools import combinations, permutations, product
from collections import Counter, deque

input = [ list(map(int, l.strip().split())) for l in open(0) ]

def safe(l):
    diff = [i - j for i, j in zip(l[:-1], l[1:])]
    if not all(d > 0 for d in diff) and not all(d < 0 for d in diff):
        return False
    if not all(1 <= abs(d) <= 3 for d in diff):
        return False
    return True

s = sum(any(safe(l[:i] + l[i + 1:]) for i in range(len(l))) for l in input)
print(s)