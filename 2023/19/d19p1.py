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
    for r in re.findall('(\w+)(.)(\d+)(:(\w+))?', rest):
        rs += [ (r[0], r[1], int(r[2]), r[4]) ]
    final = rest.split(',')[-1]
    rules[name] = (rs, final)

cmp = {
    '<': lambda a, b : a < b,
    '>': lambda a, b : a > b,
}
ratings = 0
for p in pts.split('\n'):
    p = { r[0]: int(r[1]) for r in re.findall('(\w+)=(\d+)', p) }
    curr = 'in'
    rejected = False
    accepted = False
    print(p, sum(p.values()))
    while not accepted and not rejected:
        rs, final = rules[curr]
        print(' ', curr, rs, final)
        redirected = False
        for r in rs:
            if cmp[r[1]](p[r[0]], r[2]):
                dest = r[3]
                if dest == 'A':
                    accepted = True
                elif dest == 'R':
                    rejected = True
                else:
                    redirected = True
                    curr = dest
                break
        print('  ', redirected, accepted, rejected, curr)
        if not redirected and not accepted and not rejected:
            if final == 'A':
                accepted = True
            elif final == 'R':
                rejected = True
            else:
                curr = final
    if accepted:
        print('  accept')
        ratings += sum(p.values())

print(ratings)







