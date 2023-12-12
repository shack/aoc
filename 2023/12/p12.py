import re
import math
from functools import reduce, cmp_to_key
from itertools import combinations, permutations, product
from collections import Counter

def combs(a, b):
    cache = {}
    def cached_work(a, b, last_was_hash):
        k = (a, tuple(b), last_was_hash)
        if k in cache:
            return cache[k]
        else:
            res = work(a, b, last_was_hash)
            cache[k] = res
            return res

    def work(a, b, last_was_hash):
        if len(a) == 0:
            if last_was_hash:
                return b == [ 0 ]
            else:
                return len(b) == 0
        if a[0] == '.':
            if last_was_hash:
                if b[0] != 0:
                    return 0
                else:
                    return cached_work(a[1:], b[1:], False)
            else:
                return cached_work(a[1:], b, False)
        elif a[0] == '#':
            if len(b) == 0:
                return 0
            elif b[0] == 0:
                return 0
            else:
                return cached_work(a[1:], [b[0] - 1] + b[1:], True)
        elif a[0] == '?':
            return cached_work('#' + a[1:], b, last_was_hash) \
                 + cached_work('.' + a[1:], b,  last_was_hash)

    return cached_work(a, b, False)

def p1(input):
    n = 0
    for l in input:
        a, b = l.split(' ')
        b = [ int(i) for i in b.split(',') ]
        n += combs(a, b)
    print(n)

def p2(input):
    n = 0
    for l in input:
        a, b = l.split(' ')
        b = [ int(i) for i in b.split(',') ] * 5
        a = '?'.join([a] * 5)
        n += combs(a, b)
    print(n)

input = [ l.strip() for l in open(0) ]

p1(input)
p2(input)