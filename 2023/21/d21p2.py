input = [ l.strip() for l in open(0) ]
assert len(input) == len(input[0]), 'input must be square'
n = len(input)
k = n // 2

start = next((x, y) for y, l in enumerate(input) for x, c in enumerate(l) if c == 'S')

def moves(x, y):
    for dx, dy in ((0, 1), (0, -1), (1, 0), (-1, 0)):
        nx, ny = (x + dx) % n, (y + dy) % n
        if input[ny][nx] != '#':
            yield x + dx, y + dy

curr = set()
curr.add(start)
lens = []
for i in range(3 * n):
    lens.append(len(curr))
    next = set()
    for x, y in curr:
        next |= set(moves(x, y))
    curr = next

a, b, c = lens[k], lens[n + k], lens[2 * n + k]
N = 26501365 // n
print(a + N * (b-a) + N * (N-1) * (c - b - b + a) // 2)