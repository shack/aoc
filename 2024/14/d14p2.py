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

cnt = 0
while True:
    s = set((px, py) for px, py in pos)
    if len(s) == len(pos):
        print(cnt)
        break
    for i, (p, (vx, vy)) in enumerate(zip(pos, vel)):
        nx, ny = p[0] + vx, p[1] + vy
        if not (0 <= nx < X):
            nx %= X
        if not (0 <= ny < Y):
            ny %= Y
        p[0], p[1] = nx, ny
    cnt += 1