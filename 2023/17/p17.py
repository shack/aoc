from heapq import heappush, heappop

def search(map, new_nn):
    q = [ (0, 0, 0, 1, 0, 0), (0, 0, 0, 0, 1, 0) ]
    seen = set()
    solutions = []
    while q:
        d, x, y, dx, dy, n = heappop(q)
        if (x, y) == (X - 1, Y - 1):
            solutions.append((n, d))
        for ndx, ndy in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
            if (ndx, ndy) == (-dx, -dy):
                continue
            nx = x + ndx
            ny = y + ndy
            if not (0 <= nx < X) or not (0 <= ny < Y):
                continue
            nn, skip = new_nn((dx, dy), (ndx, ndy), n)
            if skip:
                continue
            nd = map[ny][nx] + d
            m = (nx, ny, ndx, ndy, nn)
            if not m in seen:
                heappush(q, (nd,) + m)
                seen.add(m)
    return solutions

def p1(input):
    def new_nn(dir, new_dir, n):
        nn = n + 1 if dir == new_dir else 1
        return (nn, nn > 3)
    solutions = search(input, new_nn)
    print(min(d for n, d in solutions))

def p2(input):
    def new_nn(dir, new_dir, n):
        if dir == new_dir:
            nn = n + 1
            return (nn, nn > 10)
        else:
            return (1, n < 4)
    solutions = search(input, new_nn)
    print(min(d for n, d in solutions if n >= 4))

input = [ [ int(i) for i in l.strip() ] for l in open(0) ]
X = len(input[0])
Y = len(input)

p1(input)
p2(input)