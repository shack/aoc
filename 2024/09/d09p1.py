import re
import math
from functools import reduce, cmp_to_key
from itertools import combinations, permutations, product
from collections import Counter, deque

input = [ l.strip() for l in open(0) ][0]
map = []
occ = input[0::2]
free = input[1::2]
for i, (o, f) in enumerate(zip(occ, free)):
    map += [i] * int(o)
    map += [-1] * int(f)
if len(occ) > len(free):
    map += [i + 1] * int(occ[-1])

def next_free(pos, free):
    pos += 1
    while pos < len(free) and free[pos] != -1:
        pos += 1
    return pos

def last_occ(pos, occ):
    pos -= 1
    while pos >= 0 and occ[pos] == -1:
        pos -= 1
    return pos

f = 0
o = len(map)
res = 0
while True:
    o = last_occ(o, map)
    f = next_free(f, map)
    if o <= f:
        print(sum(i * a for i, a in enumerate(map[:o+1])))
        break
    map[f] = map[o]
    map[o] = -1