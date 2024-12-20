import re
import math
import heapq
from functools import reduce, cmp_to_key, cache
from itertools import combinations, permutations, product
from collections import Counter, deque

input = [ list(l.strip()) for l in open(0) ]
X, Y = len(input[0]), len(input)
valid_coords = set()

for y, row in enumerate(input):
    for x, cell in enumerate(row):
        if cell in 'SE.':
            valid_coords.add((x, y))
        if cell == 'S':
            start = (x, y)
        elif cell == 'E':
            end = (x, y)

def astar(start, valid_coords, heur):
    q = []
    visited = { start: 0 }
    src = {}

    heapq.heappush(q, (heur(start), start))
    while q:
        h, curr = heapq.heappop(q)
        c = h - heur(curr)
        if curr in visited and visited[curr] < c:
            continue

        for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            np = (curr[0] + dx, curr[1] + dy)
            if np in valid_coords:
                new_c = c + 1
                new_h = new_c + heur(np)
                if np not in visited or visited[np] > new_c:
                    src[np] = curr
                    visited[np] = new_c
                    heapq.heappush(q, (new_h, np))
    return visited, src

l1 = lambda p, q: abs(p[0] - q[0]) + abs(p[1] - q[1])
heur = lambda p: l1(p, end)
dists, _ = astar(start, valid_coords, lambda p: 0)
print(dists)


q = dists
cnt = 0
for a, b in combinations(q, 2):
    cheat = l1(a, b)
    orig = q[b] - q[a]
    if cheat <= 20 and orig - cheat >= 100:
        cnt += 1
print(cnt)