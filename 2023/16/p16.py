def change_dir(map, b):
    x, y, dx, dy = b
    c = map[y][x]
    if dx != 0:
        if c == '|':
            return [(x, y, 0, 1), (x, y, 0, -1)]
        elif c == '/':
            return [(x, y, 0, -dx)]
        elif c == '\\':
            return [(x, y, 0, dx)]
        else:
            return [(x, y, dx, dy)]
    elif dy != 0:
        if c == '-':
            return [(x, y, 1, 0), (x, y, -1, 0)]
        elif c == '/':
            return [(x, y, -dy, 0)]
        elif c == '\\':
            return [(x, y, dy, 0)]
        else:
            return [(x, y, dx, dy)]
    return b

def move(map, b):
    x, y, dx, dy = b
    nx, ny = x + dx, y + dy
    m = len(map)
    return (nx, ny, dx, dy) if 0 <= nx < m and 0 <= ny < m else None

def simulate(input, b):
    q = [ b ]
    seen = { b }
    while len(q) > 0:
        b = q.pop(0)
        bs = change_dir(input, b)
        for b in bs:
            b = move(input, b)
            if b and b not in seen:
                q.append(b)
                seen.add(b)
    seen = { (x, y) for x, y, _, _ in seen }
    return len(seen)

def p1(input):
    print(simulate(input, (0, 0, 1, 0)))

def p2(input):
    assert len(input) == len(input[0])
    res = 0
    m = len(input) - 1
    for i in range(m + 1):
        a = simulate(input, (i, 0, 0, 1))
        b = simulate(input, (i, m, 0, -1))
        c = simulate(input, (0, i, 1, 0))
        d = simulate(input, (m, i, -1, 0))
        res = max(res, a, b, c, d)
    print(res)

input = [ list(l.strip()) for l in open(0) ]

p1(input)
p2(input)