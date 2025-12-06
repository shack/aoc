input = [ l.replace('\n', ' ') for l in open(0) ]
w = max(max(map(len, l)) for l in [ line.split() for line in input ])
indices = [ i for i, c in enumerate(input[-1]) if c != ' ' ] + [ len(input[0]) + 1 ]
input = [ [ l[a:b-1] for a, b in zip(indices[:-1], indices[1:]) ] for l in input ]
ops = [ o.strip() for o in input[-1] ]
input = input[:-1]

n_cols = len(input[0])

res = [ [ '' for _ in range(n_cols) ] for __ in range(w) ]
for c in range(n_cols):
    for j in range(len(input[0][c])):
        for r in range(len(input)):
            res[j][c] += input[r][c][j]

input = res
res = [ int(x) for x in input[0] ]
for line in input[1:]:
    assert len(line) == len(ops)
    for i, _ in enumerate(res):
        if x := line[i].strip():
            match ops[i]:
                case '+':
                    res[i] += int(x)
                case '*':
                    res[i] *= int(x)

print(sum(res))
