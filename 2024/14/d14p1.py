import re
import math
from functools import reduce, cmp_to_key
from itertools import combinations, permutations, product
from collections import Counter, deque

pos = []
vel = []
for x in re.findall(r'p=(-?\d+),(-?\d+) v=(-?\d+),(-?\d+)', open(0).read()):
    px, py, vx, vy = tuple(map(int, x))
    pos.append([px, py])
    vel.append((vx, vy))

Y = 103
X = 101

for i in range(100):
    for p, (vx, vy) in zip(pos, vel):
        nx, ny = p[0] + vx, p[1] + vy
        if not (0 <= nx < X):
            nx %= X
        if not (0 <= ny < Y):
            ny %= Y
        p[0], p[1] = nx, ny

qs = [ 0, 0, 0, 0 ]
for px, py in pos:
    if px == X // 2 or py == Y // 2:
        continue
    if px < X // 2 and py < Y // 2:
        qs[0] += 1
    elif px >= X // 2 and py < Y // 2:
        qs[1] += 1
    elif px < X // 2 and py >= Y // 2:
        qs[2] += 1
    else:
        qs[3] += 1

print(reduce(lambda x, y: x * y, qs, 1))