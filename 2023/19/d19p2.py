import sys
import re
from operator import mul
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

def search(name, bounds):
    if name == 'A':
        return reduce(mul, (b[1] - b[0] for b in bounds.values()))
    elif name == 'R':
        return 0
    res = 0
    rs, final = rules[name]
    for n, c, v, d in rs:
        l, u = bounds[n]
        assert l <= v < u
        if c == '<':
            t, f = (l, v), (v, u)
        else:
            f, t = (l, v + 1), (v + 1, u)
        if t[1] - t[0] > 0:
            b = dict(bounds)
            b[n] = t
            res += search(d, b)
        bounds[n] = f
    return res + search(final, bounds)

bounds = { k: (1, 4001) for k in 'xmas' }
print(search('in', bounds))






