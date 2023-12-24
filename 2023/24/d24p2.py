import re
from z3 import *

input = [ tuple(map(int, re.findall(r'-?\d+', l))) for l in open(0) ]

qx = Real('qx')
qy = Real('qy')
qz = Real('qz')
px = Real('px')
py = Real('py')
pz = Real('pz')
solver = Solver()
ts = []
for i, (x, y, z, dx, dy, dz) in enumerate(input):
     t = Real(f't{i}')
     ts.append(t)
     solver.add(x + t * dx == px + t * qx)
     solver.add(y + t * dy == py + t * qy)
     solver.add(z + t * dz == pz + t * qz)
     solver.add(t >= 0)
solver.check()
m = solver.model()
print(m[px].as_long() + m[py].as_long() + m[pz].as_long())





