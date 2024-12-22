import re
import math
from functools import reduce, cmp_to_key
from itertools import combinations, permutations, product
from collections import Counter, deque

def sim(x, n):
    def mix_prune(n, m):
        return (n ^ m) & 16777215
    for _ in range(n):
        x = mix_prune(x, x << 6)
        x = mix_prune(x, x >> 5)
        x = mix_prune(x, x << 11)
    return x

input = [ l.strip() for l in open(0) ]

res = 0
for x in input:
    s = sim(int(x), 2000)
    res += s
    print(x, s)
print(res)