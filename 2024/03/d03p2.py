import re
import math
from functools import reduce, cmp_to_key
from itertools import combinations, permutations, product
from collections import Counter, deque

input = [ l.strip() for l in open(0) ]
s = 0
active = True
for l in input:
    for r in re.findall(r'(mul\((\d+),(\d+)\)|don\'t\(\)|do\(\))', l):
        match r[0][0:3]:
            case "mul":
                if active:
                    x, y = int(r[1]), int(r[2])
                    assert x < 1000 and y < 1000
                    s += x * y
            case "don":
                active = False
            case "do(":
                active = True
print(s)



