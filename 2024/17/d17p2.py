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
    vers = [1, 0, 0]

    def upd(reg, val):
        regs[reg] = BitVec(f'r{reg}_v{vers[reg]}', width)
        vers[reg] += 1
        s.add(regs[reg] == val)

    for _ in range(max_loop):
        ip = 0
        while ip < len(prg):
            i = prg[ip]
            lit = prg[ip+1]
            assert lit != 7
            if lit <= 3:
                combo = BitVecVal(lit, width)
            else:
                combo = regs[lit-4]
            match i:
                case 0:
                    upd(0, LShR(regs[0], combo))
                    ip += 2
                case 1:
                    upd(1, regs[1] ^ lit)
                    ip += 2
                case 2:
                    upd(1, combo & 7)
                    ip += 2
                case 3:
                    break
                case 4:
                    upd(1, regs[1] ^ regs[2])
                    ip += 2
                case 5:
                    o = BitVec(f'o{len(out)}', width)
                    out.append(o)
                    s.add(o == combo & 7)
                    ip += 2
                case 6:
                    upd(1, LShR(regs[0], combo))
                    ip += 2
                case 7:
                    upd(2, LShR(regs[0], combo))
                    ip += 2
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