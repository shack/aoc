bricks = []
X, Y = 0, 0
for l in open(0):
    l, r = l.strip().split('~')
    a = tuple(map(int, l.split(',')))
    b = tuple(map(int, r.split(',')))
    X = max(X, a[0], b[0])
    Y = max(Y, a[1], b[1])
    assert len(set([*a, *b])) <= 4
    bricks += [ (a, b) ]

bricks = sorted(bricks, key=lambda b : min(b[0][2], b[1][2]))

M = {}
supports = { k: set() for k in range(len(bricks)) }
for i, ((x1, y1, z1), (x2, y2, z2)) in enumerate(bricks):
    x1, x2 = sorted([x1, x2])
    y1, y2 = sorted([y1, y2])
    z1, z2 = sorted([z1, z2])
    below = []
    B = [ (x, y) for x in range(x1, x2 + 1) for y in range(y1, y2 + 1) ]
    below = [ M[c] for c in B if c in M ]
    if len(below) > 0:
        below = sorted(below, key=lambda b : b[1], reverse=True)
        max_z = below[0][1]
        for b, z in below:
            if z == max_z:
                supports[b] |= { i }
    else:
        max_z = 0
    for c in B:
        M[c] = (i, max_z + z2 - z1 + 1)

n_disintegrate = 0
n_no_support = 0
for i in range(len(bricks)):
    this = set(supports[i])
    if len(this) == 0:
        n_no_support += 1
    else:
        other = [ supports[j] for j in range(0, len(bricks)) if i != j]
        other = set.union(*other) if other else set()
        n_disintegrate += len(this & other) == len(this)
print(n_disintegrate + n_no_support)

