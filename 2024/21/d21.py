from functools import cache
from itertools import permutations

num_pos = {
    '7': (0, 0), '8': (1, 0), '9': (2, 0),
    '4': (0, 1), '5': (1, 1), '6': (2, 1),
    '1': (0, 2), '2': (1, 2), '3': (2, 2),
                 '0': (1, 3), 'A': (2, 3),
}

key_pos = {
                 '^': (1, 0), 'A': (2, 0),
    '<': (0, 1), 'v': (1, 1), '>': (2, 1),
}

dirs = {
    '<': (-1, 0), 'v': (0, 1), '>': (1, 0), '^': (0, -1),
}

def valid_seq(seq, pad, pos):
    x, y = pos
    for d in seq:
        dx, dy = dirs[d]
        x, y = x + dx, y + dy
        if not (x, y) in pad.values():
            return False
    return True

def min_len(seq, depth, max_depth):
    pad = num_pos if depth == 0 else key_pos
    return sum(min_ab(pad[a], pad[b], depth, max_depth) for a, b in zip('A' + seq[:-1], seq))

@cache
def min_ab(fr, to, depth, max_depth):
    if fr == to:
        return 1
    x, y = fr
    nx, ny = to
    pad = num_pos if depth == 0 else key_pos
    keys = ''
    if nx > x:
        keys += '>' * (nx - x)
    if nx < x:
        keys += '<' * (x - nx)
    if ny > y:
        keys += 'v' * (ny - y)
    if ny < y:
        keys += '^' * (y - ny)
    if depth >= max_depth:
        return len(keys) + 1
    res = 100000000000000000000
    for p in permutations(keys):
        if valid_seq(p, pad, fr):
            l = min_len(''.join(p) + 'A', depth + 1, max_depth)
            res = min(res, l)
    return res


input = open(0).read().splitlines()

def sol(max_depth):
    res = 0
    for l in input:
        num = int(l[:3])
        res += num * min_len(l, 0, max_depth)
    return res

print(sol(2))
print(sol(25))








