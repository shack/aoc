import re
import sys
from functools import reduce

def p1():
    def find(l, v):
        for d, s, r in l:
            if v >= s and v < s + r:
                return d + v - s
        return v
    total = 0
    maps = []
    for l in open(sys.argv[1], 'r'):
        l = l.strip()
        if re.match('^seeds: ', l):
            _, l = l.split(':')
            seeds = [ int(x) for x in l.split() ]
        if m := re.match('(\w+)-to-(\w+) map:', l):
            maps.append(ranges := [])
            continue
        elif m := re.match('(\d+) (\d+) (\d+)', l):
            d, s, r = map(int, [ m[1], m[2], m[3] ])
            ranges += [ (d, s, r) ]
            continue
    locs = []
    for e in seeds:
        for m in maps:
            e = find(m, e)
        locs.append(e)
    print(min(locs))

def p2():
    def find(l, S, R):
        res = set()
        E = S + R
        min_b = E
        max_e = S
        for d, s, r in l:
            e = min(s + r, E)
            b = max(s, S)
            if e <= b:
                continue
            min_b = min(min_b, b)
            max_e = max(max_e, e)
            res.add((d + b - s, e - b))
        if min_b > S:
            res.add((S, min_b - S))
        if max_e < E:
            res.add((max_e, E - max_e))
        return list(res)

    maps = []
    for l in open(sys.argv[1], 'r'):
        l = l.strip()
        if re.match('^seeds: ', l):
            _, l = l.split(':')
            seeds = [ int(x) for x in l.split() ]
        if m := re.match('(\w+)-to-(\w+) map:', l):
            maps.append(ranges := [])
            continue
        elif m := re.match('(\d+) (\d+) (\d+)', l):
            d, s, r = map(int, [ m[1], m[2], m[3] ])
            ranges += [ (d, s, r) ]
            continue
    maps = [ sorted(m, key=lambda x: x[1]) for m in maps ]
    seed_base = seeds[::2]
    seed_range = seeds[1::2]
    locs = []
    for b, r in zip(seed_base, seed_range):
        rs = [ (b, r) ]
        for i, m in enumerate(maps):
            res = []
            for b, r in rs:
                res += find(m, b, r)
            rs = res
        locs += rs
    print(min(s for s, _ in locs))

p1()
p2()


