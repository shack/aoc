import re
import sys
from functools import reduce

def p1():
    total = 0
    for l in open(sys.argv[1], 'r'):
        l = l.strip()
        _, lr = l.split(':')
        w, h = lr.split('|')
        res = 1
        w = set(int(x) for x in w.strip().split())
        h = set(int(x) for x in h.strip().split())
        e = len(w & h)
        total += pow(2, e - 1) if e > 0 else 0
    print(total)

def p2():
    wins = {}
    for i, l in enumerate(open(sys.argv[1], 'r')):
        l = l.strip()
        _, lr = l.split(':')
        w, h = lr.split('|')
        w = set(int(x) for x in w.strip().split())
        h = set(int(x) for x in h.strip().split())
        wins[i] = len(w & h)
    nc = { i: 1 for i in range(len(wins)) }
    for i in range(len(wins)):
        cs = nc[i]
        for _ in range(cs):
            for j in range(wins[i]):
                idx = i + j + 1
                if idx < len(wins):
                    nc[idx] += 1
    print(sum(nc.values()))

p1()
p2()


