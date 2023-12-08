import re
import sys
from functools import reduce, cmp_to_key
from collections import Counter

def p1():
    with open(sys.argv[1], 'r') as f:
        lines = f.readlines()
        dirs = lines[0].strip()
        g = {}
        for p in lines[2:]:
            p = p.strip()
            m = re.match('(\w+) = \((\w+), (\w+)\)', p)
            n = m[1]
            l = m[2]
            r = m[3]
            g[n] = (l, r)

    n = 'AAA'
    cnt = 0
    while True:
        for d in dirs:
            n = g[n][0 if d == 'L' else 1]
            cnt += 1
            if n == 'ZZZ':
                print(cnt)
                return


def p2():
    with open(sys.argv[1], 'r') as f:
        lines = f.readlines()
        dirs = lines[0].strip()
        g = {}
        for p in lines[2:]:
            p = p.strip()
            m = re.match('(\w+) = \((\w+), (\w+)\)', p)
            n = m[1]
            l = m[2]
            r = m[3]
            g[n] = (l, r)

    def walk(n):
        cnt = 0
        while True:
            for d in dirs:
                n = g[n][0 if d == 'L' else 1]
                cnt += 1
                if n[2] == 'Z':
                    return cnt

    start = [ x for x in dict.keys(g) if x[2] == 'A' ]
    n = 'AAA'
    cnts = []
    for n in start:
        cnt = walk(n)
        cnts += [ cnt ]

    import math
    print(math.lcm(*cnts))

p1()
p2()


