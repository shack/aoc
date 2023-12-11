import re
import math
from functools import reduce, cmp_to_key
from itertools import combinations, permutations, product
from collections import Counter

def transpose(matrix):
    return list(map(list, zip(*matrix)))

def twice(input):
    res = []
    for l in input:
        if not '#' in l:
            res += [l]
        res += [l]

    rest = transpose(res)
    res = []
    for l in rest:
        if not '#' in l:
            res += [l]
        res += [l]
    return transpose(res)

abs = lambda x: x if x >= 0 else -x

def p1(input):
    uni = twice(input)
    galaxies = list()
    for y, l in enumerate(uni):
        for x, c in enumerate(l):
            if c == '#':
                galaxies += [(x, y)]

    res = 0
    for (x0, y0), (x1, y1) in combinations(galaxies, 2):
        d = abs(x1 - x0) + abs(y1 - y0)
        res += d
    print(res)

def p2(input):
    rows = set(i for i, l in enumerate(input) if not '#' in l)
    cols = set(i for i, l in enumerate(transpose(input)) if not '#' in l)
    size = 1000000
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

p1(input)
p2(input)