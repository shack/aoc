import re
import math
from functools import cache, reduce, cmp_to_key
from itertools import combinations, permutations, product
from collections import Counter, deque, defaultdict

def area(a, b):
    x0, y0 = a
    x1, y1 = b
    return (abs(x0 - x1) + 1) * (abs(y0 - y1) + 1)

def sort(v):
    (px, py), (qx, qy) = v
    return (min(px, qx), min(py, qy)), (max(px, qx), max(py, qy))

input = [ tuple(map(int, l.strip().split(','))) for l in open(0) ]
poly  = list(map(sort, zip(input, input[1:] + input[0:1])))

res = 0
for (ax, ay), (bx, by) in map(sort, combinations(input, 2)):
    size = area((ax, ay), (bx, by))
    if size > res:
        for (px, py), (qx, qy) in poly:
            if ax < qx and ay < qy and bx > px and by > py:
                break
        else:
            res = max(res, size)

print(res)