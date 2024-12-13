import re
import sys
from z3 import *

offset = 10000000000000 if len(sys.argv) > 1 and sys.argv[1] == '2' else 0
input = [ b.split('\n') for b in open(0).read().split('\n\n') ]
tokens = 0
for l in input:
    ax, ay = re.findall(r'X\+(\d+), Y\+(\d+)', l[0])[0]
    bx, by = re.findall(r'X\+(\d+), Y\+(\d+)', l[1])[0]
    x,  y   = re.findall(r'X=(\d+), Y=(\d+)', l[2])[0]
    ax, ay = int(ax), int(ay)
    bx, by = int(bx), int(by)
    x,  y  = int(x) + offset, int(y) + offset
    a, b = Reals('a b')
    s = Optimize()
    s.add(ax * a + bx * b == x)
    s.add(ay * a + by * b == y)
    s.minimize(3*a+b)
    if s.check() == sat:
        try:
            a = s.model()[a].as_long()
            b = s.model()[b].as_long()
            tokens += 3 * a + b
        except:
            pass
print(tokens)


