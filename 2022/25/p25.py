import sys, math
from functools import reduce

digits = [ '=', '-', '0', '1', '2' ]

def snafu_to_decimal(snafu):
    base = 1
    res = 0
    for d in reversed(snafu):
        res += (digits.index(d) - 2) * base
        base *= 5
    return res

def decimal_to_snafu(d):
    e = 0
    while d > 5 ** e:
        e += 1
    res = [0] * (e + 1)
    while e >= 0:
        p = d // (5 ** e)
        res[e] = p
        r = int(d % (5 ** e))
        d = r
        e -= 1

    for i in range(len(res)):
        if res[i] > 2:
            res[i] -= 5
            res[i + 1] += 1

    if res[-1] == 0:
        res = res[:-1]
    return reduce(lambda r, d: r + digits[d + 2], reversed(res), '')

res = sum(snafu_to_decimal(i.strip()) for i in sys.stdin.readlines())
print(res)
snafu = decimal_to_snafu(res)
print(snafu)
        


