import re
import sys
from functools import reduce

sample = [
    (7, 9), (15, 40), (30, 200)
]

input = [
    (34, 204), (90, 1713), (89, 1210), (86, 1780)
]

def winning(time, dist, hold):
    return hold * (time - hold) > dist

def n_wins(time, dist):
    return sum(1 for h in range(time) if winning(time, dist, h))

def p1():
    print(reduce(lambda x, y: x * y, [ n_wins(time, dist) for time, dist in input ]))

def p2():
    time = ""
    dist = ""
    for t, d in input:
        time += str(t)
        dist += str(d)
    print(n_wins(int(time), int(dist)))

p1()
p2()


