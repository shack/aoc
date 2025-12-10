import re
import math
from z3 import *
from functools import reduce, cmp_to_key
from itertools import combinations, permutations, product
from collections import Counter, deque, defaultdict
from queue import PriorityQueue

input = [ l.strip().split() for l in open(0) ]
input = [ (tuple(eval(l[-1][1:-1])), list(map(eval, l[1:-1]))) for l in input ]

def solve(goal, buttons):
    s = Optimize()
    xs = [ Int(f'x{i}') for i, _ in enumerate(buttons) ]
    s.minimize(sum(xs))
    for x in xs:
        s.add(x >= 0)
    for i, g in enumerate(goal):
        e = IntVal(0)
        for x, b in zip(xs, buttons):
            if i in b:
                e += x
        s.add(e == g)
    res = s.check()
    assert res == sat
    m = s.model()
    return sum(m[x].as_long() for x in xs)

res = 0
for i, l in enumerate(input):
    goal = l[0]
    buttons = [ (b,) if type(b) == int else b for b in l[1] ]
    res += solve(goal, buttons)
print(res)