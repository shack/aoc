import sys, copy, re

def dist(ax, ay, bx, by):
    return abs(ax - bx) + abs(ay - by)

sensors = []
for l in sys.stdin.readlines():
    c = re.findall(r'x=(-?\d+), y=(-?\d+)', l)
    sx, sy = int(c[0][0]), int(c[0][1])
    bx, by = int(c[1][0]), int(c[1][1])
    d = dist(sx, sy, bx, by)
    sensors += [(sx, sy, d)]

y = 2000000
no = set()
for sx, sy, d in sensors:
    dx = d - abs(sy - y)
    if dx >= 0:
        for x in range(sx - dx, sx + dx):
            no.add(x)
print(len(no))

max_y = 4000000
for y in range(0, max_y + 1):
    intv = []
    for sx, sy, d in sensors:
        dx = d - abs(sy - y)
        if dx >= 0:
            l = max(0, sx - dx)
            u = min(max_y, sx + dx)
            intv += [(l, u)]
    intv = sorted(intv, key=lambda i: i[0])
    x = 0
    for l, u in intv:
        if x + 1 < l:
            break
        x = max(x, u)
    if x < max_y:
        print((x + 1) * max_y + y)
