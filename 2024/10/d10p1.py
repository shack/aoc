import re
import math
from functools import reduce, cmp_to_key
from itertools import combinations, permutations, product
from collections import Counter, deque

input = [ list(map(int, l.strip())) for l in open(0) ]
X, Y = len(input), len(input[0])

def search(x, y, h):
    if x < 0 or x >= X or y < 0 or y >= Y:
        return
    if (input[y][x]) == h:
        if (input[y][x]) == 9:
            yield (x, y)
        else:
            next = [ (0, 1), (1, 0), (0, -1), (-1, 0) ]
            for dx, dy in next:
                yield from search(x + dx, y + dy, h + 1)
    return

score = 0
for y in range(Y):
    for x in range(X):
        if input[y][x] == 0:
            reach = set((t for t in search(x, y, 0)))
            score += len(reach)
print(score)