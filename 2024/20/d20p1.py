import re
import math
import heapq
from functools import reduce, cmp_to_key, cache
from itertools import combinations, permutations, product
from collections import Counter, deque

input = [ list(l.strip()) for l in open(0) ]
valid_coords = set()
walls = set()
X, Y = len(input[0]), len(input)

for y, row in enumerate(input):
    for x, cell in enumerate(row):
        if cell in 'SE.':
            valid_coords.add((x, y))
        if cell == 'S':
            start = (x, y)
        elif cell == 'E':
            end = (x, y)
        elif cell == '#':
            walls.add((x, y))

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

dists, _ = astar(start, valid_coords, lambda p: 0)
time = dists[end]

cnt = 0
for wx, wy in walls:
    valid_coords.add((wx, wy))
    dists, _ = astar(start, valid_coords, lambda p: 0)
    if dists[end] <= time - 100:
        cnt += 1
    valid_coords.remove((wx, wy))
print(cnt)