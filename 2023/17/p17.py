import re
import math
from functools import reduce, cmp_to_key
from itertools import combinations, permutations, product
from collections import Counter, deque

def empty(*args, **kwargs):
    pass

def search(map, x, y):
    R270 = [ [ 0, 1 ], [ -1, 0 ] ]
    R90 = [ [ 0, -1 ], [ 1, 0 ] ]
    I = [ [ 1, 0 ], [ 0, 1 ] ]
    q = deque([ (x, y, 1, 0, 0, 0) ])
    seen = {}
    solutions = set()
    N = len(map)
    assert N == len(map[0])
    debug = empty
    while len(q) > 0:
        x, y, dx, dy, n, d = q.popleft()
        debug(x, y, '    ', dx, dy, n, d)
        if x == N - 1 and y == N - 1:
            solutions.add(d)
        for M in [ R90, R270, I ]:
            ndx = dx * M[0][0] + dy * M[0][1]
            ndy = dx * M[1][0] + dy * M[1][1]
            nx = x + ndx
            ny = y + ndy
            if not (0 <= nx < N) or not (0 <= ny < N):
                continue
            debug(' ', nx, ny, end=' ')
            nn = n + 1 if (ndx, ndy) == (dx, dy) else 1
            if nn >= 4:
                debug('too long')
                continue
            nd = map[ny][nx] + d
            m = (nx, ny, ndx, ndy, nn)
            if not m in seen or seen[m] > nd:
                q.append(m + (nd,))
                seen[m] = nd
                debug('append new')
            else:
                debug('drop')
    # print(solutions)
    print(min(solutions))

def search2(map, x, y):
    R270 = [ [ 0, 1 ], [ -1, 0 ] ]
    R90 = [ [ 0, -1 ], [ 1, 0 ] ]
    I = [ [ 1, 0 ], [ 0, 1 ] ]
    q = deque([ (x, y, 1, 0, 0, 0) ])
    seen = {}
    solutions = set()
    N = len(map)
    assert N == len(map[0])
    debug = empty
    while len(q) > 0:
        x, y, dx, dy, n, d = q.popleft()
        debug(x, y, '    ', dx, dy, n, d)
        if x == N - 1 and y == N - 1:
            solutions.add(d)
        for M in [ R90, R270, I ]:
            ndx = dx * M[0][0] + dy * M[0][1]
            ndy = dx * M[1][0] + dy * M[1][1]
            nx = x + ndx
            ny = y + ndy
            if not (0 <= nx < N) or not (0 <= ny < N):
                continue
            debug(' ', nx, ny, end=' ')
            if (ndx, ndy) == (dx, dy):
                nn = n + 1
                if nn > 10:
                    debug('too long')
                    continue
            elif n < 4:
                debug('too short')
                continue
            else:
                nn = 1
            nd = map[ny][nx] + d
            m = (nx, ny, ndx, ndy, nn)
            if not m in seen or seen[m] > nd:
                q.append(m + (nd,))
                seen[m] = nd
                debug('append new')
            else:
                debug('drop')
    # print(solutions)
    print(min(solutions))

def p1(input):
    search(input, 0, 0)
    pass

def p2(input):
    search2(input, 0, 0)
    pass

input = [ [ int(i) for i in l.strip() ] for l in open(0) ]

p1(input)
p2(input)