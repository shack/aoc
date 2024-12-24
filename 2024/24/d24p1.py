from functools import cache

g = {}
init, gates = open(0).read().split('\n\n')
for l in init.split('\n'):
    w, v = l.split(': ')
    g[w] = int(v)
for l in gates.split('\n'):
    x, op, y, _, z = l.split()
    g[z] = (x, op, y)

@cache
def sim(w):
    match g[w]:
        case (x, 'AND', y):
            return sim(x) & sim(y)
        case (x, 'OR', y):
            return sim(x) | sim(y)
        case (x, 'XOR', y):
            return sim(x) ^ sim(y)
        case v:
            return v

out = sorted([ w for w in g if w.startswith('z') ], reverse=True)
print(int(''.join(str(sim(w)) for w in out), 2))



