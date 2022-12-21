import sys

shapes = [
    [ '@@@@' ],

    [ ' @ ',
      '@@@',
      ' @ ' ],

    [ '@@@',
      '  @',
      '  @' ],

    [ '@',
      '@',
      '@',
      '@' ],

    [ '@@',
      '@@' ],
]

new = [ ' ' for i in range(0, 7) ]

def collision(cave, shape, x, y):
    for r in shape:
        if y >= len(cave):
            continue
        for i, s in enumerate(r):
            if s != ' ' and cave[y][x + i] != ' ':
                return True
        y += 1
    return False

def put(cave, shape, x, y):
    ext = max(y + len(shape) - len(cave), 0)
    cave += [ list(new) for i in range(0, ext) ]
    for r in shape:
        assert y < len(cave)
        for i, s in enumerate(r):
            if s != ' ':
                assert cave[y][x + i]
                cave[y][x + i] = '#'
        y += 1

def print_cave(cave):
    for y in range(len(cave) - 1, -1, -1):
        print(''.join(cave[y]).replace(' ', '.'))

def simulate(n_pieces, cave = [], idx = 0):
    height = 0
    states = {}
    p = 0
    while p < n_pieces:
        assert len(cave) == 0 or cave[len(cave) - 1].count(' ') < len(new)
        curr_shape = p % len(shapes)

        # through away irrelevant parts of the cave
        if len(cave) > 0:
            min_y = len(cave)
            for x in range(0, len(cave[0])):
                first_block = 0
                for y in range(len(cave) - 1, -1, -1):
                    if cave[y][x] != ' ':
                        first_block = y
                        break
                # print(first_block, end='')
                min_y = min(min_y, first_block)
            height += min_y
            cave = cave[min_y:]
            cave_str = '\n'.join([ ''.join(r) for r in cave ])
            st = (cave_str, curr_shape, idx)
            if st in states:
                old_height, old_p = states[st]
                diff_pieces = p - old_p
                n_repetitions = (n_pieces - p) // diff_pieces
                add_height = n_repetitions * (height - old_height)
                # print('p', p, 'n_p', n_pieces, 'diff pieces', diff_pieces, 'rep', n_repetitions, \
                # 'height', height, 'add height', add_height)
                p += diff_pieces * n_repetitions
                height += add_height
            else:
                states[st] = (height, p)

        # new stone emerges
        shape = shapes[curr_shape]
        y = len(cave) + 3
        x = 2

        while True:
            m, idx = moves[idx], (idx + 1) % len(moves)
            if m == '<':
                nx = max(x - 1, 0)
            elif m == '>':
                nx = min(len(new) - len(shape[0]), x + 1)
            if not collision(cave, shape, nx, y):
                x = nx
            if y == 0 or collision(cave, shape, x, y - 1):
                put(cave, shape, x, y)
                break
            else:
                y -= 1
        p += 1
    return height + len(cave)

moves = sys.stdin.readline()

print(simulate(2022))

big = 1000000000000

print(simulate(big))