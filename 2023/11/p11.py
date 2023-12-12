import re
import math
from functools import reduce, cmp_to_key
from itertools import combinations, permutations, product
from collections import Counter

# matrix transpose
def transpose(m):
    return list(map(list, zip(*m)))

def solve(input, size):
    rows = set(i for i, l in enumerate(input) if not '#' in l)
    cols = set(i for i, l in enumerate(transpose(input)) if not '#' in l)
    galaxies = list()
    for y, l in enumerate(input):
        for x, c in enumerate(l):
            if c == '#':
                galaxies += [(x, y)]
    res = 0
    for (x0, y0), (x1, y1) in combinations(galaxies, 2):
        x = sorted([ x0, x1 ])
        y = sorted([ y0, y1 ])
        for c, p in zip([x, y], [cols, rows]):
            pump = len(set(range(c[0], c[1])) & p)
            res += c[1] - c[0] - pump + size * pump
    print(res)

input = [ l.strip() for l in open(0) ]

solve(input, 2)
solve(input, 1000000)