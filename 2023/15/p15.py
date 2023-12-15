import re
import math
from functools import reduce, cmp_to_key
from itertools import combinations, permutations, product
from collections import Counter

def hash(s):
    f = lambda r, c: (17 * (r + ord(c))) % 256
    return reduce(f, s, 0)

def p1(input):
    print(reduce(lambda r, p: r + hash(p), input, 0))

def p2(input):
    boxes = dict()
    for p in input:
        if p[-1] == '-':
            l = p[:-1]
            b = hash(l)
            if b in boxes and l in boxes[b]:
                del boxes[b][l]
        else:
            l, i = p.split('=')
            b = hash(l)
            if not b in boxes:
                boxes[b] = dict()
            boxes[b][l] = int(i)
    res = 0
    for b, ls in boxes.items():
        for i, (l, f) in enumerate(ls.items()):
            res += (1 + b) * (i + 1) * f
    print(res)

input = open(0).readlines()[0].split(',')

p1(input)
p2(input)