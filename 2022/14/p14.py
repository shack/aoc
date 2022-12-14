import sys, copy

def plot(cave, sx, sy):
    for y in range(0, 30):
        for x in range(480, 520):
            if y == sy and x == sx:
                print('o', end='')
            else:
                print(cave[y][x], end='')
        print()
    
def place(cave, sx, sy):
    if cave[sy + 1][sx] == ' ':
        return sx, sy + 1
    elif cave[sy + 1][sx - 1] == ' ':
        return sx - 1, sy + 1
    elif cave[sy + 1][sx + 1] == ' ':
        return sx + 1, sy + 1
    else:
        cave[sy][sx] = 'o'
        return sx, sy

def p1(cave):
    units = 0
    while True:
        sx, sy = 500, 0
        try: 
            while True:
                sx, sy = place(cave, sx, sy)
                if cave[sy][sx] == 'o':
                    units += 1
                    break
        except IndexError:
            print(units)
            return

def p2(cave, max_y):
    for x in range(0, len(cave[0])):
        cave[max_y + 2][x] = '#'
    units = 0
    while True:
        sx, sy = 500, 0
        units += 1
        while True:
            sx, sy = place(cave, sx, sy)
            if cave[sy][sx] == 'o':
                if sx == 500 and sy == 0:
                    print(units)
                    return
                else:
                    break

cave = [ [ ' ' for i in range(0, 1000) ] for y in range(0, 200) ]
max_y = 0
for l in sys.stdin.readlines():
    lx, ly = 0, 0
    for i, c in enumerate(l.split('->')):
        cx, cy = [ int(a) for a in c.split(',') ]
        max_y = max(max_y, cy)
        if i > 0:
            if cx == lx:
                s, e = sorted([ly, cy])
                for y in range(s, e + 1):
                    cave[y][cx] = '#'
            elif cy == ly:
                s, e = sorted([lx, cx])
                for x in range(s, e + 1):
                    cave[cy][x] = '#'
            else:
                assert False
        lx, ly = cx, cy

cave2 = copy.deepcopy(cave)
p1(cave)
p2(cave2, max_y)