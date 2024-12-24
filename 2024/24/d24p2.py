g = {}
ins = set()
init, gates = open(0).read().split('\n\n')
for l in init.split('\n'):
    w, v = l.split(': ')
    ins.add(w)
for l in gates.split('\n'):
    x, op, y, _, z = l.split()
    g[z] = (x, op, y)

print('digraph G {')
for z, (x, op, y) in g.items():
    print(f'  {z} -> {x}')
    print(f'  {z} -> {y}')
    print(f'  {z} [label="{z} {op}"]')
print('}')

# manual inspection of the graph