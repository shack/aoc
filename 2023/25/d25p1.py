from itertools import combinations

import networkx as nx
G = nx.DiGraph()

nodes = set()
for i, l in enumerate(open(0)):
    l, r = l.strip().split(':')
    r = r.split()
    nodes.add(l)
    for n in r:
        G.add_edge(l, n, capacity=1)
        G.add_edge(n, l, capacity=1)

for n, m in combinations(nodes, 2):
    cut_value, partition = nx.minimum_cut(G, n, m)
    if cut_value == 3:
        assert len(partition) == 2
        print(len(partition[0]) * len(partition[1]))
        break