import re
import sys
from functools import reduce, cmp_to_key
from collections import Counter

def diffs(ns):
    x = ns[0]
    for y in ns[1:]:
        yield y - x
        x = y

def ext(ns):
    last = [ns[-1]]
    while not all(x == 0 for x in ns):
        ns = list(diffs(ns))
        last.append(ns[-1])
    last.reverse()
    x = last[0]
    for y in last[1:]:
        x += y
    return x

def extl(ns):
    first = [ns[0]]
    while not all(x == 0 for x in ns):
        ns = list(diffs(ns))
        first.append(ns[0])
    first.reverse()
    x = first[0]
    for y in first[1:]:
        x = y - x
    return x

def p1():
    with open(sys.argv[1], 'r') as f:
        res = 0
        for l in f:
            ns = [int(x) for x in l.split()]
            res += ext(ns)
        print(res)


def p2():
    with open(sys.argv[1], 'r') as f:
        res = 0
        for l in f:
            ns = [int(x) for x in l.split()]
            res += extl(ns)
        print(res)
    pass

p1()
p2()


