import re
import sys
from functools import reduce

def p1():
    sum = 0
    f = open(sys.argv[1], 'r')
    p = [ l.strip() for l in f ]
    vx = lambda x: x >= 0 and x < len(p[0])
    vy = lambda y: y >= 0 and y < len(p)
    issym = lambda c: c != '.' and not c.isdigit()
    r = re.compile('\d+')
    for i, l in enumerate(p):
        for m in r.finditer(l):
            s, e = m.span()
            n = int(m.group())
            ok = False
            for x in range(s - 1, e + 1):
                for y in range(i - 1, i + 2):
                    if vx(x) and vy(y) and issym(p[y][x]):
                        ok = True
                        break
            if ok:
                sum += n
    print(sum)


def p2():
    sum = 0
    gears = {}
    f = open(sys.argv[1], 'r')
    p = [ l.strip() for l in f ]
    vx = lambda x: x >= 0 and x < len(p[0])
    vy = lambda y: y >= 0 and y < len(p)
    r = re.compile('\d+')
    for i, l in enumerate(p):
        for m in r.finditer(l):
            s, e = m.span()
            n = int(m.group())
            for x in range(s - 1, e + 1):
                for y in range(i - 1, i + 2):
                    if vx(x) and vy(y) and p[y][x] == '*':
                        if (x, y) in gears:
                            sum += gears[(x, y)] * n
                            del gears[(x, y)]
                        else:
                            gears[(x, y)] = n
    print(sum)

p1()
p2()


