import re
import math
from functools import reduce, cmp_to_key, cache
from itertools import combinations, permutations, product, pairwise
from collections import Counter, deque, defaultdict
from queue import PriorityQueue

def get_blocks(input):
    blocks = []
    curr = []
    for l in input:
        if l:
            curr += [ l ]
        else:
            blocks += [ curr ]
            curr = []
    return blocks + [ curr ]

blocks = get_blocks([ l.strip() for l in open(0) ])
presents = [ l[1:] for l in blocks[:-1] ]

configs = []
for l in blocks[-1]:
    ls = l.split()
    m = re.match(r'(\d+)x(\d+):', ls[0])
    cfg = [ m.group(1), m.group(2) ] + ls[1:]
    configs += [ [ int(x) for x in cfg ] ]

def area(p):
    return sum(sum(1 for x in row if x == '#') for row in p)

res = 0
for cfg in configs:
    ps = [ (i, c) for i, c in enumerate(cfg[2:]) if c > 0 ]
    board = [ ['.'] * cfg[0] for _ in range(cfg[1]) ]
    lower = sum(area(presents[i]) * c for i, c in ps)
    too_much = lower >= cfg[0] * cfg[1]
    fits_trivially = sum(c for _, c in ps) <= (cfg[0] // 3) * (cfg[1] // 3)
    assert fits_trivially or too_much
    res += fits_trivially

print(res)