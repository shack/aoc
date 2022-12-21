import sys, copy, re

edges = {}
rates = {}

for l in sys.stdin.readlines():
    l = l.rstrip()
    l, r = l.split(';')
    l = l.strip().split(' ')
    r = r.strip().split(' ')
    rates[l[1]] = int(l[4].split('=')[1])
    edges[l[1]] = [ v.replace(',', '') for v in r[4:] ]

# floyd warshall
infty = 100000000
dist = {}
for v, n in edges.items():
    dist[(v, v)] = 0
    for w in n:
        dist[(v, w)] = 1
for k in edges:
    for i in edges:
        for j in edges:
            dist[(i, j)] = min(dist.get((i, j), infty), dist.get((i, k), infty) + dist.get((k, j), infty))

def search(v, t, rest):
    max_p = 0
    for i, w in enumerate(rest):
        d = dist[(v, w)]
        if d < t:
            nr = rest[0:i] + rest[i+1:]
            rt = t - d - 1
            p = rates[w] * rt + search(w, rt, nr)
            max_p = max(max_p, p)
    return max_p

def search_e(v, t, rest):
    max_p = 0
    for i, w in enumerate(rest):
        d = dist[(v, w)]
        if d < t:
            nr = rest[0:i] + rest[i+1:]
            rt = t - d - 1
            p = rates[w] * rt + search_e(w, rt, nr)
            max_p = max(max_p, p)
    if max_p == 0 and len(rest) > 0:
        return search('AA', 26, rest)
    return max_p

valves = [ v for v in rates if rates[v] > 0 ]
print(search('AA', 30, valves))

valves = [ v for v in rates if rates[v] > 0 ]
print(search_e('AA', 26, valves))

