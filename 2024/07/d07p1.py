import re
import math
from functools import reduce, cmp_to_key
from itertools import combinations, permutations, product
from collections import Counter, deque

input = [ l.strip() for l in open(0) ]
ans = 0
for l in input:
    res, right = l.split(': ')
    nums = list(map(int, right.split(' ')))
    res = int(res)

    ok = False
    fst = nums[0]
    rest = nums[1:]
    for ops in product(*(['+*'] * (len(rest)))):
        r = fst
        for n, op in zip(rest, ops):
            match op:
                case '+': r += n
                case '*': r *= n
        if r == res:
            ok = True
            break
    if ok:
        ans += res
print(ans)