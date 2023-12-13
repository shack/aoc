import re
import math
from functools import reduce, cmp_to_key
from itertools import combinations, permutations, product
from collections import Counter

def transpose(m):
    return list(map(list, zip(*m)))

def dist(p, q):
    return sum(a != b for a, b in zip(p, q))

def is_reflect(m, row, bnd):
    d = min(row, len(m) - row)
    l = m[row:row + d]
    u = m[row - d:row]
    u = list(reversed(u))
    return sum(dist(a, b) for a, b in zip(l, u)) == bnd

def find_reflect(m, bnd):
    for i in range(1, len(m)):
        if is_reflect(m, i, bnd):
            return i
    return 0

def p1(input):
    res = 0
    for m in input:
        res += 100 * find_reflect(m, 0)
        res += find_reflect(transpose(m), 0)
    print(res)

def p2(input):
    res = 0
    for m in input:
        res += find_reflect(m, 1)
        res += find_reflect(transpose(m), 1)
    print(res)

input = [ l.split('\n') for l in open(0).read().split('\n\n') ]

p1(input)
p2(input)