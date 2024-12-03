import re
import math
from functools import reduce, cmp_to_key
from itertools import combinations, permutations, product
from collections import Counter, deque

input = [ l.strip() for l in open(0) ]
print(sum(int(x) * int(y) for l in input for x, y in re.findall(r'mul\((\d+),(\d+)\)', l)))



