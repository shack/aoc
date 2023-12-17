from heapq import heappush, heappop

def search(map, new_nn):
    L = [ [ 0, 1 ], [ -1, 0 ] ]
    R = [ [ 0, -1 ], [ 1, 0 ] ]
    I = [ [ 1, 0 ], [ 0, 1 ] ]
    dirs = [ L, R, I ]
    q = [ (0, 0, 0, 1, 0, 0) ]
    seen = {}
    while q:
        d, x, y, dx, dy, n = heappop(q)
        for M in dirs:
            ndx = dx * M[0][0] + dy * M[0][1]
            ndy = dx * M[1][0] + dy * M[1][1]
            nx = x + ndx
            ny = y + ndy
            if not (0 <= nx < X) or not (0 <= ny < Y):
                continue
            nn, skip = new_nn((x, y), (dx, dy), (ndx, ndy), n)
            if skip:
                continue
            nd = map[ny][nx] + d
            m = (nx, ny, ndx, ndy, nn)
            if not m in seen or seen[m] > nd:
                heappush(q, (nd,) + m)
                seen[m] = nd
    return seen

def p1(input):
    def new_nn(pos, dir, new_dir, n):
        nn = n + 1 if dir == new_dir else 1
        return (nn, nn > 3)
    seen = search(input, new_nn)
    print(min([ seen[m] for m in seen if m[:2] == (X - 1, Y - 1) ]))

def p2(input):
    def new_nn(pos, dir, new_dir, n):
        if dir == new_dir:
            nn = n + 1
            return (nn, nn > 10)
        else:
            return (1, pos != (0, 0) and n < 4)
    seen = search(input, new_nn)
    print(min([ seen[m] for m in seen if m[:2] == (X - 1, Y - 1) and m[4] >= 4]))

input = [ [ int(i) for i in l.strip() ] for l in open(0) ]
X = len(input[0])
Y = len(input)

p1(input)
p2(input)