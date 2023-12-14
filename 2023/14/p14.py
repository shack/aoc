import re
import math
from functools import reduce, cmp_to_key
from itertools import combinations, permutations, product
from collections import Counter

def tilt_north(input):
    def find_pos(row, col):
        r = row - 1
        while r >= 0:
            if input[r][col] == '.':
                r -= 1
            else:
                return r + 1
        return 0
    for row, l in enumerate(input):
        for col, c in enumerate(l):
            if c == 'O':
                r = find_pos(row, col)
                if r < row:
                    input[r][col] = 'O'
                    input[row][col] = '.'

def weight(input):
    res = 0
    for i, l in enumerate(input):
        w = len(input) - i
        n = sum(c == 'O' for c in l)
        res += w * n
    return res

def map_to_str(input):
    return '\n'.join([''.join(l) for l in input])

def print_map(input):
    print(map_to_str(input))

def p1(input):
    tilt_north(input)
    print(weight(input))

def cycle(input):
    def transpose(input):
        return [ list(l) for l in zip(*input) ]

    # north
    tilt_north(input)

    # west
    input = transpose(input)
    tilt_north(input)
    input = transpose(input)

    # south
    input.reverse()
    tilt_north(input)
    input.reverse()

    # east
    input = transpose(input)
    input.reverse()
    tilt_north(input)
    input.reverse()
    input = transpose(input)

    return input

def p2(input):
    m = list(map(list, input))
    n = 1000000000
    seen = {}
    for i in range(n):
        s = map_to_str(input)
        if s in seen:
            start = seen[s]
            repeat = i - start - 1
            break
        else:
            seen[s] = i
        input = cycle(input)
    rest = n % repeat
    for i in range(start + repeat + rest):
        m = cycle(m)
    print(weight(m))

input = [ [ c for c in l.strip() ] for l in open(0) ]

p1(input)
p2(input)