import sys, re, itertools, collections

def add(a, b):
    return [ x + y for x, y in zip(a, b) ]

def sub(a, b):
    return [ x - y for x, y in zip(a, b) ]

def one(dim, i):
    assert i < dim
    res = [0] * dim
    res[i] = 1
    return res

class Blueprint:
    def __init__(self, values):
        self.id = values[0]
        self.costs = [
            [ values[1], 0, 0, 0 ],
            [ values[2], 0, 0, 0 ],
            [ values[3], values[4], 0, 0 ],
            [ values[5], 0, values[6], 0 ],
        ]

        self.maxr = [ 
            max(values[2], values[3], values[5]),
            values[4],
            values[6],
            1000000
        ]
        self.cache = {}

    def search(self, t, max_geodes, res, rob):
        def build(r, max_geodes):
            nonlocal self, t, res, rob
            c = sub(res, self.costs[r])
            if all(x >= 0 for x in c):
                nr = rob[:]
                nr[r] += 1
                return (True, self.search(t - 1, max_geodes, add(c, rob), nr))
            return (False, 0)

        k = (t, *res, *rob)
        if k in self.cache:
            return self.cache[k]
        m = res[3] + rob[3] * t

        # assuming we can build a geode robot in every remaining step ...
        if m + t * (t - 1) // 2 < max_geodes: 
            return max_geodes
        if t == 0:
            return res[3]

        m = max(m, self.search(t - 1, max(max_geodes, m), add(res, rob), rob))
        for r in [3, 2, 1, 0]:
            if rob[r] < self.maxr[r]:
                b, mb  = build(r, m)
                m = max(m, mb)
                # if we could build a geode robot, don't do anything else
                if b and r == 3:
                    break
        self.cache[k] = m
        return m

bps = []
for i, l in enumerate(sys.stdin.readlines()):
    v = list(map(int, re.findall(r'(\d+)', l)))
    bps.append(Blueprint(v))

res = 0
for bp in bps:
    g = bp.search(24, 0, [0, 0, 0, 0], [1, 0, 0, 0])
    res += bp.id * g
    print(bp.id, g)
print(res)

res = 1
for bp in bps:
    if bp.id == 3:
        break
    g = bp.search(32, 0, [0, 0, 0, 0], [1, 0, 0, 0])
    res *= g
    print(bp.id, g)
print(res)
