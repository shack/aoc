import re
import math
from functools import reduce, cmp_to_key
from itertools import combinations, permutations, product
from collections import Counter, deque

input = [ l.strip() for l in open(0) ]

print(input)
for y, l in enumerate(input):
    if (x := l.find('S')) != -1:
        start = (x, y)
        break

def moves(x, y):
    for dx, dy in ((0, 1), (0, -1), (1, 0), (-1, 0)):
        if 0 <= x + dx < len(input[0]) \
            and 0 <= y + dy < len(input) \
            and input[y + dy][x + dx] != '#':
            yield (x + dx, y + dy)

curr = set()
curr.add(start)
for i in range(64):
    next = set()
    for x, y in curr:
        next |= set(moves(x, y))
    curr = next
print(len(curr))

