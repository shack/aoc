import re
import math
from functools import reduce, cmp_to_key
from itertools import combinations, permutations, product
from collections import Counter, deque, defaultdict


input = [ list(l.strip()) for l in open(0) ]
X = len(input[0])
Y = len(input)
antennas = defaultdict(list)
inrange = lambda x, y: 0 <= x < X and 0 <= y < Y
for y, l in enumerate(input):
    for x, c in enumerate(l):
        if c != '.':
            antennas[c].append((x, y))

antinodes = set()
for _, ant in antennas.items():
    for (ax, ay), (bx, by) in combinations(ant, 2):
        dx, dy = ax - bx, ay - by
        while inrange(ax + dx, ay + dy):
            antinodes.add((ax + dx, ay + dy))
            ax += dx
            ay += dy
        while inrange(bx + dx, by + dy):
            antinodes.add((bx + dx, by + dy))
            bx -= dx
            by -= dy
print(len(antinodes))

