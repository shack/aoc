import sys
import re
import math
from functools import reduce, cmp_to_key
from itertools import combinations, permutations, product
from collections import Counter

wfs, pts = open(0).read().split('\n\n')
rules = {}
for wf in wfs.split('\n'):
    wf = wf[:-1]
    name, rest = wf.split('{')
    rs = []
    for r in re.findall('(\w+)(.)(\d+):(\w+)?', rest):
        rs += [ (r[0], r[1], int(r[2]), r[3]) ]
    final = rest.split(',')[-1]
    rules[name] = rs + [("x", 't', 0, final)]

cmp = {
    '<': lambda a, b : a < b,
    '>': lambda a, b : a > b,
    't': lambda a, b : True,
}

def eval_wf(name, p):
    for v, c, n, d in rules[name]:
        if cmp[c](p[v], n):
            match d:
                case 'A':
                    return sum(p.values())
                case 'R':
                    return 0
                case _:
                    return eval_wf(d, p)

ratings = 0
for p in pts.split('\n'):
    p = { r[0]: int(r[1]) for r in re.findall('(\w+)=(\d+)', p) }
    ratings += eval_wf('in', p)
print(ratings)