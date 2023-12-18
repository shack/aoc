import re
import math
from functools import reduce, cmp_to_key
from itertools import combinations, permutations, product
from collections import Counter

# Let 'vertices' be an array of N pairs (x,y), indexed from 0
# Let 'area' = 0.0
# for i = 0 to N-1, do
#   Let j = (i+1) mod N
#   Let area = area + vertices[i].x * vertices[j].y
#   Let area = area - vertices[i].y * vertices[j].x
# end for
# Return 'area'

def p1(input):
    x, y = 1000000000, 1000000000
    area = 0
    perimeter = 0
    for d, n, _ in input:
        n = int(n)
        perimeter += n
        nx, ny = x, y
        if d == 'L':
            nx -= n
        elif d == 'R':
            nx += n
        elif d == 'U':
            ny -= n
        elif d == 'D':
            ny += n
        area += x * ny
        area -= y * nx
        x, y = nx, ny
    print((area + perimeter) // 2 + 1)

def p2(input):
    x, y = 1000000000, 1000000000
    area = 0
    perimeter = 0
    dir = 'RDLU'
    for _, _, c in input:
        c = c[2:-1]
        d = dir[int(c[-1])]
        n = int(c[:-1], 16)
        perimeter += n
        nx, ny = x, y
        if d == 'L':
            nx -= n
        elif d == 'R':
            nx += n
        elif d == 'U':
            ny -= n
        elif d == 'D':
            ny += n
        area += x * ny
        area -= y * nx
        x, y = nx, ny
    print((area + perimeter) // 2 + 1)

input = [ l.strip().split() for l in open(0) ]

p1(input)
p2(input)