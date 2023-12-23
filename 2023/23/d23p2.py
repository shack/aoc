input = [ l.strip() for l in open(0) ]
N = len(input)
assert N == len(input[0])
start = (0, 1)
end = (N - 2, N - 1)

def neighs(x, y):
    for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
        nx, ny = x + dx, y + dy
        if 0 <= nx < N and 0 <= ny < N and input[ny][nx] != '#':
            yield nx, ny

# find hubs
hubs = { start: {}, end: {} }
for y, l in enumerate(input):
    for x, c in enumerate(l):
        if c != '#':
            if sum(1 for _ in neighs(x, y)) > 2:
                hubs[(x, y)] = {}

# find path length between hubs
for hx, hy in hubs:
    q = [(hx, hy, 0)]
    seen = set((hx, hy))
    while q:
        x, y, n = q.pop()
        if (x, y) in hubs and n > 0:
            hubs[(hx, hy)][(x, y)] = n
        else:
            for nx, ny in neighs(x, y):
                if not (nx, ny) in seen:
                    q.append((nx, ny, n + 1))
                    seen.add((nx, ny))

low = -1000000000000
def search(seen, curr):
    if curr == end:
        return 0
    seen.add(curr)
    res = max((d + search(seen, n) for n, d in hubs[curr].items() \
               if not n in seen), default=low)
    seen.remove(curr)
    return res

print(search(set(), start))