import re
import math
from functools import reduce, cmp_to_key
from itertools import combinations, permutations, product
from collections import Counter, deque

input = [ l.strip() for l in open(0) ]

def find_start():
    for y, l in enumerate(input):
        for x, c in enumerate(l):
            match c:
                case '<': return x, y, -1, 0
                case '>': return x, y, 1, 0
                case '^': return x, y, 0, -1
                case 'v': return x, y, 0, 1
                case _:
                    pass

x, y, dx, dy = find_start()
N = len(input)
pos = set()
while True:
    pos.add((x, y))
    nx, ny = x + dx, y + dy
    if not (0 <= nx < N and 0 <= ny < N):
        break
    elif input[ny][nx] == '#':
        dx, dy = -dy, dx
    else:
        x, y = x + dx, y + dy
print(len(pos))