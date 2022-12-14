
def cmp(x, y):
    return (x > y) - (x < y)

def compare(l, r):
    if type(l) == int and type(r) == int:
        return cmp(l, r)
    elif type(l) == list and type(r) == list:
        for x, y in zip(l, r):
            if c := compare(x, y):
                return c
        return cmp(len(l), len(r))
    elif type(l) == int:
        assert type(r) == list
        return compare([l], r)
    elif type(r) == int:
        assert type(l) == list
        return compare(l, [r])

import functools

inp = [ l.split() for l in open(0).read().split('\n\n') ]
inp = [ [ eval(l) for l in p ] for p in inp ]

# Part 1
sum = 0
for i, (l, r) in enumerate(inp):
    sum += i + 1 if compare(l, r) < 0 else 0
print(sum)

# Part 2
all = [ [[2]], [[6]] ]
for p in inp:
    all += p
all = sorted(all, key=functools.cmp_to_key(compare))
res = 1
for i, l in enumerate(all):
    if l == [[2]] or l == [[6]]:
        res *= i + 1
print(res)
