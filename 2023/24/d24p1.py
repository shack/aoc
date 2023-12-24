import re
from itertools import combinations

input = [ tuple(map(int, re.findall(r'-?\d+', l))) for l in open(0) ]

def intersect(a, b):
    def sign(x):
        return 1 if x > 0 else -1 if x < 0 else 0
    x0, y0, _, dx0, dy0, _ = a
    x1, y1, _, dx1, dy1, _ = b

    q = dx1 * dy0 - dx0 * dy1
    if q == 0:
        return None
    p = dx0 * dx1 * (y1 - y0) - dy1 * dx0 * x1 + dy0 * dx1 * x0
    x = p / q
    y = dy0 * x / dx0 + y0 - dy0 * x0 / dx0
    if (x - x0) / dx0 > 0 and (x - x1) / dx1 > 0:
        return (x, y)
    else:
        return None

n = 0
l = 200000000000000
u = 400000000000000
for a, b in combinations(input, 2):
    r = intersect(a, b)
    if r:
        x, y = r
        if l <= x <= u and l <= y <= u:
            n += 1
print(n)