def input(name='input.txt'):
    with open(name, 'rt') as f:
        for l in f:
            yield l.rstrip()

def read_world():
    res = []
    for l in input():
        res += [ l ]
    return res

def is_visible(grid, tx, ty):
    max_x = len(grid[0])
    max_y = len(grid)
    height = grid[ty][tx];
    ok = 4
    for x in range(tx + 1, max_x):
        if grid[ty][x] >= height:
            ok = ok - 1
            break
    for x in range(0, tx):
        if grid[ty][x] >= height:
            ok = ok - 1
            break
    for y in range(0, ty):
        if grid[y][tx] >= height:
            ok = ok - 1
            break
    for y in range(ty + 1, max_y):
        if grid[y][tx] >= height:
            ok = ok - 1
            break
    return 1 if ok > 0 else 0

def p1():
    grid = read_world()
    dx = len(grid[0])
    dy = len(grid)
    cnt = 2 * dx + 2 * dy - 4
    for y in range(1, dy - 1):
        for x in range(1, dx - 1):
            cnt += is_visible(grid, x, y)
    print(cnt)

def scenic_score(grid, tx, ty):
    max_x = len(grid[0])
    max_y = len(grid)
    height = grid[ty][tx];
    score_r = 0
    score_l = 0
    score_u = 0
    score_d = 0
    for x in range(tx + 1, max_x):
        score_r = score_r + 1
        if grid[ty][x] >= height:
            break
    for x in range(tx - 1, -1, -1):
        score_l = score_l + 1
        if grid[ty][x] >= height:
            break
    for y in range(ty - 1, -1, -1):
        score_u = score_u + 1
        if grid[y][tx] >= height:
            break
    for y in range(ty + 1, max_y):
        score_d = score_d + 1
        if grid[y][tx] >= height:
            break
    return score_d * score_u * score_l * score_r

def p2():
    grid = read_world()
    dx = len(grid[0])
    dy = len(grid)
    max_score = 0
    for y in range(1, dy - 1):
        for x in range(1, dx - 1):
            score = scenic_score(grid, x, y)
            if score > max_score:
                max_score = score
    print(max_score)

p1()
p2()