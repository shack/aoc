import re
import math
from functools import reduce, cmp_to_key
from itertools import combinations, permutations, product
from collections import Counter, deque

input = [ l.strip() for l in open(0) ]
input = [ line.split() for line in input ]

ops = input[-1]
input = input[:-1]
print(ops)
res = [ int(i) for i in input[0]  ]
for line in input[1:]:
    assert len(line) == len(ops)
    for i, _ in enumerate(res):
        match ops[i]:
            case '+':
                res[i] += int(line[i])
            case '*':
                res[i] *= int(line[i])

print( sum(res) )
