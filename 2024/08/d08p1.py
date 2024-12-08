import re
import math
from functools import reduce, cmp_to_key
from itertools import combinations, permutations, product
from collections import Counter, deque, defaultdict


antennas = defaultdict(list)
input = [ list(l.strip()) for l in open(0) ]
X = len(input[0])
Y = len(input)
for y, l in enumerate(input):
    for x, c in enumerate(l):
        if c != '.':
            antennas[c].append((x, y))

antinodes = set()
for _, ant in antennas.items():
    for (ax, ay), (bx, by) in combinations(ant, 2):
        dx, dy = ax - bx, ay - by
        antinodes.add((ax + dx, ay + dy))
        antinodes.add((bx - dx, by - dy))
antinodes = { (x, y) for x, y in antinodes if 0 <= x < X and 0 <= y < Y }
print(len(antinodes))

