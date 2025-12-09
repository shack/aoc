import re
import math
from functools import reduce, cmp_to_key
from itertools import combinations, permutations, product
from collections import Counter, deque, defaultdict

def area(a, b):
    x0, y0 = a
    x1, y1 = b
    return (abs(x0 - x1) + 1) * (abs(y0 - y1) + 1)

input = [ tuple(map(int, l.strip().split(','))) for l in open(0) ]
print(max(((a, b, area(a, b)) for a, b in combinations(input, 2)), key=lambda x: x[2]))


