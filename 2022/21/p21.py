import sys 

def evaluate(dag, node = "root"):
    if type(dag[node]) == int:
        return dag[node]
    else:
        l = evaluate(dag, dag[node][0])
        r = evaluate(dag, dag[node][2])
        return dag[node][1](l, r)

def solve(dag, parent, node):
    p = parent[node]
    is_left = dag[p][0] == node
    other = dag[p][2] if is_left else dag[p][0]
    v = evaluate(dag, other)

    if p == "root":
        return v

    w = solve(dag, parent, p)
    op = dag[p][3]
    if op == "+":
        return w - v
    elif op == "-":
        return w + v if is_left else v - w
    elif op == "*":
        return w / v
    elif op == "/":
        return w * v if is_left else v / w


dag = {}
parent = {}
for l in sys.stdin.readlines():
    x, y = l.strip().split(":")
    expr = y.strip().split(" ")
    if len(expr) == 1:
        dag[x] = int(expr[0])
    else:
        fst = expr[0]
        snd = expr[2]
        op  = eval("lambda {}, {}: {}".format(fst, snd, y))
        dag[x] = (fst, op, snd, expr[1])
        parent[fst] = parent[snd] = x

print(evaluate(dag))
print(solve(dag, parent, "humn"))