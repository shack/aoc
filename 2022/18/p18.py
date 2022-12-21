import sys, itertools, collections

neighbors = [
    (1, 0, 0), (0, 1, 0), (0, 0, 1),
    (-1, 0, 0), (0, -1, 0), (0, 0, -1)
]

big = 100000000000

mx = big
my = big
mz = big
Mx = 0
My = 0
Mz = 0

# common sides
sides = {}
for r in sys.stdin.readlines():
    x, y, z = map(int, r.split(','))
    mx = min(mx, x)
    my = min(my, y)
    mz = min(mz, z)
    Mx = max(Mx, x)
    My = max(My, y)
    Mz = max(Mz, z)
    sides[(x, y, z)] = 0

# Part 1
for a, b in itertools.product(sides, sides):
    if sum([ abs(c - d) for c, d in zip(a, b)]) == 1:
        sides[a] += 1
        sides[b] += 1

# we counted every element twice because of itertools.product
covered = sum(sides.values()) // 2
area = 6 * len(sides) - covered
print(area)

# Part 2
mx, my, mz = mx - 1, my - 1, mz - 1
Mx, My, Mz = Mx + 1, My + 1, Mz + 1

q = collections.deque()
q.append((mx, my, mz))
surrounding = set()
while len(q) > 0:
    x, y, z = q.popleft()

    for dx, dy, dz in neighbors:
        nx, ny, nz = c = x + dx, y + dy, z + dz

        if not (mx <= nx <= Mx and my <= ny <= My and mz <= nz <= Mz):
            continue

        if c in surrounding or c in sides:
            continue

        q.append(c)
        surrounding.add(c)

surface = 0
for x, y, z in surrounding:
    for dx, dy, dz in neighbors:
        if (x + dx, y + dy, z + dz) in sides:
            surface += 1
print(surface)



