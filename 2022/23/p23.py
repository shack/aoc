import sys, copy

dirs = [
    (-1,  0),
    (-1,  1),
    ( 0,  1),
    ( 1,  1),
    ( 1,  0),
    ( 1, -1),
    ( 0, -1),
    (-1, -1),
]

N  = dirs[0]
NE = dirs[1]
E  = dirs[2]
SE = dirs[3]
S  = dirs[4]
SW = dirs[5]
W  = dirs[6]
NW = dirs[7]

ranges = [
    ([ N, NE, NW ], N),
    ([ S, SE, SW ], S),
    ([ W, NW, SW ], W),
    ([ E, NE, SE ], E),
]

def is_empty(elves, r, c, where=dirs):
    return all(not (r + dr, c + dc) in elves for dr, dc in where)

def propose(elves, r, c, round):
    rnd = round % len(ranges)
    for env, dir in ranges[rnd:] + ranges[:rnd]:
        if is_empty(elves, r, c, env):
            return r + dir[0], c + dir[1]
    return r, c

elves = set()
map = sys.stdin.readlines()
for r, row in enumerate(map):
    for c, ch in enumerate(row):
        if ch == '#':
            elves.add((r, c))

def print_map(elves):
    for r in range(len(map)):
        for c in range(len(map[0])):
            print('#' if (r, c) in elves else '.', end='')
        print()

def p1():
    mr = min(r for r, _ in elves)
    Mr = max(r for r, _ in elves) + 1
    mc = min(c for _, c in elves)
    Mc = max(c for _, c in elves) + 1
    print((Mr - mr) * (Mc - mc) - n_elves)

# print('initial state')
# print_map(elves)
n_elves = len(elves)
i = 0
old_elves = set()
while True:
    if i == 10:
        p1()
        
    dests = {}
    for r, c in elves:
        if is_empty(elves, r, c):
            nr, nc = np = r, c
        else:
            nr, nc = np = propose(elves, r, c, i)
        # print('elve', r, c, 'goes to', nr, nc)
        if not np in dests:
            dests[np] = []
        dests[np].append((r, c))

    old_elves = elves
    elves = set()
    for np, es in dests.items():
        if len(es) == 1:
            elves.add(np)
        else:
            for p in es:
                elves.add(p)

    # print('round', i)
    # print_map(elves)
    assert n_elves == len(elves), "n: {}, len: {}".format(n_elves, len(elves))
    i += 1

    if old_elves == elves:
        print(i)
        break