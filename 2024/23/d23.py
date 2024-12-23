import networkx as nx

input = [ l.strip() for l in open(0) ]
g = nx.Graph()
g.add_edges_from((line.split('-') for line in input))

res = 0
max_clique_sz = 0
max_clique = None
for c in nx.enumerate_all_cliques(g):
    l = len(c)
    if l == 3 and any(n.startswith('t') for n in c):
        res += 1
    if l > max_clique_sz:
        max_clique_sz = l
        max_clique = c
print(res)
print(','.join(sorted(max_clique)))