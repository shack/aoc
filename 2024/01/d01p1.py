input = [ l.strip() for l in open(0) ]
input = [ l.split() for l in input ]
l = [ int(l[0]) for l in input ]
r = [ int(l[1]) for l in input ]
print(sum(abs(x - y) for x, y in zip(sorted(l), sorted(r))))