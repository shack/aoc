import re
import math
from functools import reduce, cmp_to_key
from itertools import combinations, permutations, product
from collections import Counter, deque, defaultdict
from queue import PriorityQueue

def map_conf(config: str):
    return tuple(True if c == '#' else False for c in config)

input = [ l.strip().split() for l in open(0) ]
input = [ (map_conf(l[0][1:-1]), l[-1], list(map(eval, l[1:-1]))) for l in input ]

def apply(c, button):
    c = list(c)
    for b in button:
        c[b] = not c[b]
    return tuple(c)

def search(goal, buttons):
    dist = {}
    q = PriorityQueue()
    s = tuple(False for _ in range(len(goal)))
    q.put((0, s))
    while not q.empty():
        cost, curr = q.get()
        for b in buttons:
            c = apply(curr, b)
            co = cost + 1
            if c == goal:
                return co
            if not c in dist:
                dist[c] = co
                q.put((co, c))
    assert False

res = 0
for i, l in enumerate(input):
    goal = l[0]
    buttons = [ (b,) if type(b) == int else b for b in l[2] ]
    res += search(goal, buttons)
print(res)