import re
import math
from copy import copy
from functools import reduce, cmp_to_key
from itertools import combinations, permutations, product
from collections import Counter, deque

input = [ l.strip() for l in open(0) ]
q = deque()
q.append((0, 1, set()))

dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
maxlen = 0
while q:
    x, y, seen = q.popleft()
    if y == len(input) - 1 and x == len(input[0]) - 2:
        maxlen = max(maxlen, len(seen))
        continue
    if (i := 'v^><'.find(input[y][x])) != -1:
        dirs0 = [ dirs[i] ]
    else:
        dirs0 = dirs
    for dx, dy in dirs0:
        nx, ny = x + dx, y + dy
        if input[ny][nx] == '#':
            continue
        if (nx, ny) in seen:
            continue
        s = copy(seen)
        s.add((nx, ny))
        q.append((nx, ny, s))
print(maxlen)