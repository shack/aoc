from z3 import *

input = open(0).read()
rs, prg = input.split('\n\n')
rs = [ l.strip() for l in rs.split('\n') ]
prg = [ int(i) for i in prg.split(': ')[1].split(',') ]

regs = [ int(l.split(': ')[1]) for l in rs ]

def symexec(prg, s, width=32):
    out = []
    max_loop = len(prg)
    start = BitVec(f'ra_start', width)
    regs = [start, BitVecVal(0, width), BitVecVal(0, width)]

    for lp in range(max_loop):
        ip = 0
        while ip < len(prg):
            i = prg[ip]
            lit = prg[ip+1]
            assert lit != 7
            if lit <= 3:
                combo = BitVecVal(lit, width)
            else:
                combo = regs[lit-4]
            new_regs = [ BitVec(f'r{r}_lp{lp}_ip{ip}', width) for r in range(3) ]
            match i:
                case 0:
                    s.add(new_regs[0] == LShR(regs[0], combo))
                    s.add(new_regs[1] == regs[1])
                    s.add(new_regs[2] == regs[2])
                    ip += 2
                case 1:
                    s.add(new_regs[1] == regs[1] ^ lit)
                    s.add(new_regs[0] == regs[0])
                    s.add(new_regs[2] == regs[2])
                    ip += 2
                case 2:
                    s.add(new_regs[1] == (combo & 7))
                    s.add(new_regs[0] == regs[0])
                    s.add(new_regs[2] == regs[2])
                    ip += 2
                case 3:
                    break
                case 4:
                    s.add(new_regs[1] == regs[1] ^ regs[2])
                    s.add(new_regs[0] == regs[0])
                    s.add(new_regs[2] == regs[2])
                    ip += 2
                case 5:
                    s.add(new_regs[0] == regs[0])
                    s.add(new_regs[1] == regs[1])
                    s.add(new_regs[2] == regs[2])
                    o = BitVec(f'o_lp{lp}_ip{ip}', width)
                    out.append(o)
                    s.add(o == combo & 7)
                    ip += 2
                case 6:
                    s.add(new_regs[1] == LShR(regs[0], combo))
                    s.add(new_regs[0] == regs[0])
                    s.add(new_regs[2] == regs[2])
                    ip += 2
                case 7:
                    s.add(new_regs[2] == LShR(regs[0], combo))
                    s.add(new_regs[1] == regs[1])
                    s.add(new_regs[0] == regs[0])
                    ip += 2
            regs = new_regs
    return (start, out)

s = Optimize()
start, out = symexec(prg, s, width=128)
for i, o in zip(prg, out):
    s.add(o == i)
s.minimize(start)
res = s.check()
if res == sat:
    val = s.model()[start]
    print(val)