def find_path(inp, dist):
    max_y = len(inp)
    max_x = len(inp[0])
    queue = [(x, y) for x in range(0, max_x) for y in range(0, max_y)]
    while len(queue) > 0:
        pos, _ = min(enumerate(queue), key=lambda p: dist[p[1][1]][p[1][0]])
        x, y = queue.pop(pos)
        for nx, ny in [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]:
            if nx >= 0 and ny >=0 and nx < max_x and ny < max_y and ord(inp[ny][nx]) <= ord(inp[y][x]) + 1:
                dist[ny][nx] = min(dist[ny][nx], dist[y][x] + 1)

with open(0) as f:
    inp = [ list(l.rstrip()) for l in f.readlines() ]
    for y, row in enumerate(inp):
        for x, ch in enumerate(row):
            if ch == 'E':
                ex, ey = x, y
            elif ch == 'S':
                sx, sy = x, y
    inp[ey][ex] = 'z'
    inp[sy][sx] = 'a'

    max_y = len(inp)
    max_x = len(inp[0])

    # problem 1
    dist = [[max_x * max_y for x in range(max_x)] for y in range(max_y)]
    dist[sy][sx] = 0
    find_path(inp, dist)
    print(dist[ey][ex])

    # problem 2
    dist = [[max_x * max_y for x in range(max_x)] for y in range(max_y)]
    for y, row in enumerate(inp):
        for x, ch in enumerate(row):
            if ch == 'a':
                dist[y][x] = 0
    find_path(inp, dist)
    print(dist[ey][ex])








