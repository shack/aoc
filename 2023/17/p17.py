from collections import deque

def new_nn_p1(dir, new_dir, n):
    nn = n + 1 if dir == new_dir else 1
    return (nn, nn > 3)

def new_nn_p2(dir, new_dir, n):
    if dir == new_dir:
        nn = n + 1
        return (nn, nn > 10)
    else:
        return (1, n < 4)

def search(map, new_nn):
    L = [ [ 0, 1 ], [ -1, 0 ] ]
    R = [ [ 0, -1 ], [ 1, 0 ] ]
    I = [ [ 1, 0 ], [ 0, 1 ] ]
    dirs = [ L, R, I ]
    q = deque([ (0, 0, 1, 0, 0, 0) ])
    seen = {}
    N = len(map)
    assert N == len(map[0])
    while len(q) > 0:
        x, y, dx, dy, n, d = q.popleft()
        for M in dirs:
            ndx = dx * M[0][0] + dy * M[0][1]
            ndy = dx * M[1][0] + dy * M[1][1]
            nx = x + ndx
            ny = y + ndy
            if not (0 <= nx < N) or not (0 <= ny < N):
                continue
            nn, skip = new_nn((dx, dy), (ndx, ndy), n)
            if skip:
                continue
            nd = map[ny][nx] + d
            m = (nx, ny, ndx, ndy, nn)
            if not m in seen or seen[m] > nd:
                q.append(m + (nd,))
                seen[m] = nd
    print(min([ seen[m] for m in seen if m[:2] == (N - 1, N - 1) ]))

def p1(input):
    search(input, new_nn_p1)

def p2(input):
    search(input, new_nn_p2)

input = [ [ int(i) for i in l.strip() ] for l in open(0) ]

p1(input)
p2(input)