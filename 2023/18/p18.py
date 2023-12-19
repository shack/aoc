def p1(input):
    x, y = 0, 0
    area = 0
    perimeter = 0
    for d, n, _ in input:
        n = int(n)
        perimeter += n
        nx, ny = x, y
        if d == 'L':
            nx -= n
        elif d == 'R':
            nx += n
        elif d == 'U':
            ny -= n
        elif d == 'D':
            ny += n
        area += x * ny
        area -= y * nx
        x, y = nx, ny
    print((area + perimeter) // 2 + 1)

def p2(input):
    x, y = 0, 0
    area = 0
    perimeter = 0
    dir = 'RDLU'
    for _, _, c in input:
        c = c[2:-1]
        d = dir[int(c[-1])]
        n = int(c[:-1], 16)
        perimeter += n
        nx, ny = x, y
        if d == 'L':
            nx -= n
        elif d == 'R':
            nx += n
        elif d == 'U':
            ny -= n
        elif d == 'D':
            ny += n
        area += x * ny
        area -= y * nx
        x, y = nx, ny
    print((area + perimeter) // 2 + 1)

input = [ l.strip().split() for l in open(0) ]

p1(input)
p2(input)