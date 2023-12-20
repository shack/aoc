from collections import deque

net = {}
tp = {}
for l in open(0).readlines():
    left, right = l.strip().split('->')
    right = right.strip().split(', ')
    left = left.strip()
    ty = left[0]
    left = left if left == 'broadcaster' else left[1:]
    net[left] = right
    tp[left] = ty

st = {}
for s, ds in net.items():
    if tp[s] == '%':
        st[s] = False
    for d in ds:
        if d in tp and tp[d] == '&':
            if not d in st:
                st[d] = {}
            st[d][s] = False

def simulate():
    res = [ 1, 0 ]
    q = deque()
    src = 'broadcaster'
    for d in net[src]:
        q.append((src, d, False))
    while q:
        src, dest, hi = q.popleft()
        res[hi] += 1
        if not dest in tp:
            continue
        if tp[dest] == '%' and not hi:
            st[dest] = not st[dest]
            for d in net[dest]:
                msg = (dest, d, st[dest])
                q.append(msg)
        elif tp[dest] == '&':
            st[dest][src] = hi
            send = not all(st[dest].values())
            for d in net[dest]:
                msg = (dest, d, send)
                q.append(msg)
    return res

r = [ simulate() for _ in range(1000) ]
print(sum(x for x, _ in r) * sum(x for _, x in r))







