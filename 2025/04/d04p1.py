import re
import math
from functools import reduce, cmp_to_key
from itertools import combinations, permutations, product
from collections import Counter, deque

input = [ l.strip() for l in open(0) ]

res = 0
for y, row in enumerate(input):
    for x, ch in enumerate(row):
        if input[y][x] == '@':
            sum = 0
            for dx, dy in [ -1, 0 ], [ 1, 0 ], [ 0, -1 ], [ 0, 1 ], [ -1, -1 ], [ -1, 1 ], [ 1, -1 ], [ 1, 1 ]:
                nx, ny = x + dx, y + dy
                if 0 <= ny < len(input) and 0 <= nx < len(row):
                    sum += input[ny][nx] == '@'
            res += sum < 4
print(res)