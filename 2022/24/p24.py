import sys, collections, math

dirs = {
    '^': (-1, 0),
    '>': (0, 1),
    'v': (1, 0), 
    '<': (0, -1),
}

map   = [ r[1:-2] for r in sys.stdin.readlines() ][1:-1]
R     = len(map)
C     = len(map[0])
start = (-1, 0)
end   = (R, C - 1)
lcm   = R * C // math.gcd(R, C)

blizzards = { d: set() for d in dirs }
for r, row in enumerate(map):
    for c, d in enumerate(row):
        if d in dirs:
            blizzards[d].add((r, c))

def print_board(blizzards, r, c, t):
    for rr in range(R):
        for cc in range(C):
            bs = []
            for d, b in blizzards.items():
                dr, dc = dirs[d]
                tr = (rr - dr * t) % R
                tc = (cc - dc * t) % C
                if (tr, tc) in b:
                    bs.append(d)
            if len(bs) == 0:
                print('.', end='')
            elif len(bs) == 1:
                print(bs[0], end='')
            else:
                print(len(bs), end='')
        print()

def search(start, end, t):
    valid = set([ start, end ])
    move = list(dirs.values()) + [ (0, 0) ]
    q = collections.deque()
    q.append((t, start[0], start[1]))
    seen = set()
    while q:
        t, r, c = q.popleft()
        t += 1
        pos = []
        for dr, dc in move:
            nr = r + dr
            nc = c + dc

            if (nr, nc) == end:
                return t

            if not (0 <= nr < R and 0 <= nc < C or (nr, nc) in valid):
                continue

            if (nr, nc) == start:
                pos.append(start)
            else:
                for d, b in blizzards.items():
                    dr, dc = dirs[d]
                    tr = (nr - dr * t) % R
                    tc = (nc - dc * t) % C
                    if (tr, tc) in b:
                        break
                else:
                    pos.append((nr, nc))

        pos.sort(key=lambda p: abs(p[0] - end[0]) + abs(p[1] - end[1]))
        for nr, nc in pos:
            k = (t % lcm, nr, nc)
            if not k in seen:
                q.append((t, nr, nc))
                seen.add(k)

a = search(start, end, 0)
print(a)
b = search(end, start, a)
c = search(start, end, b)
print(c)