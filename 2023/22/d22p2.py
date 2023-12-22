from collections import deque
from copy import deepcopy

bricks = []
for l in open(0):
    l, r = l.strip().split('~')
    a = tuple(map(int, l.split(',')))
    b = tuple(map(int, r.split(',')))
    bricks += [ (a, b) ]

bricks = sorted(bricks, key=lambda b : min(b[0][2], b[1][2]))

M = {}
supported_by = { k: set() for k in range(len(bricks)) }
supports = deepcopy(supported_by)
for i, ((x1, y1, z1), (x2, y2, z2)) in enumerate(bricks):
    x1, x2 = sorted([x1, x2])
    y1, y2 = sorted([y1, y2])
    z1, z2 = sorted([z1, z2])
    B = [ (x, y) for x in range(x1, x2 + 1) for y in range(y1, y2 + 1) ]
    below = [ M[c] for c in B if c in M ]
    if len(below) > 0:
        max_z = max(z for _, z in below)
        below = filter(lambda b : b[1] == max_z, below)
        for b, z in below:
            supported_by[i] |= { b }
            supports[b] |= { i }
    else:
        max_z = 0
    for c in B:
        M[c] = (i, max_z + z2 - z1 + 1)

n_fall = 0
for i in range(len(bricks)):
    s = deepcopy(supported_by)
    q = deque([i])
    while q:
        r = q.popleft()
        for j in supports[r]:
            if r in s[j]:
                if len(s[j]) == 1:
                    q.append(j)
                    n_fall += 1
                s[j].remove(r)
print(n_fall)