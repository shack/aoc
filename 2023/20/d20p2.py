import math
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

final = 'rx'
sink = [ p for p, ds in net.items() if final in ds ]
assert len(sink) == 1
sink = sink[0]
sink_preds = set(src for src, ds in net.items() if sink in ds)
first = {}
n_press = 0
while True:
    n_press += 1
    q = deque()
    src = 'broadcaster'
    for d in net[src]:
        q.append((src, d, False))
    while q:
        src, dest, hi = q.popleft()
        if dest == sink and hi:
            if not src in first:
                first[src] = n_press
            if len(first) == len(sink_preds):
                print(math.lcm(*first.values()))
                exit(0)
        if not dest in tp:
            assert dest == final
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