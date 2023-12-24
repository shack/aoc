import re
from z3 import *

qx, qy, qz = Reals('qx qy qz')
px, py, pz = Reals('px py pz')
solver = Solver()
for i, l in enumerate(open(0)):
     x, y, z, dx, dy, dz = map(int, re.findall(r'-?\d+', l))
     t = Real(f't{i}')
     solver.add(x + t * dx == px + t * qx)
     solver.add(y + t * dy == py + t * qy)
     solver.add(z + t * dz == pz + t * qz)
     solver.add(t >= 0)
solver.check()
m = solver.model()
print(m[px].as_long() + m[py].as_long() + m[pz].as_long())





