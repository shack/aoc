
input = open(0).read()
rs, prg = input.split('\n\n')
rs = [ l.strip() for l in rs.split('\n') ]
prg = [ int(i) for i in prg.split(': ')[1].split(',') ]

regs = [ int(l.split(': ')[1]) for l in rs ]
print(regs, prg)

def op(o):
    assert o != 7
    if o <= 3:
        return o
    else:
        return regs[o-4]

out = []
ip = 0
while ip < len(prg):
    i = prg[ip]
    lit = prg[ip+1]
    combo = op(lit)
    print(i, lit, combo, regs, out)
    match i:
        case 0:
            regs[0] >>= combo
            ip += 2
        case 1:
            regs[1] ^= lit
            ip += 2
        case 2:
            regs[1] = (combo & 7)
            ip += 2
        case 3:
            if regs[0]:
                ip = lit
            else:
                ip += 2
        case 4:
            regs[1] ^= regs[2]
            ip += 2
        case 5:
            out.append(combo & 7)
            ip += 2
        case 6:
            regs[1] = regs[0] >> combo
            ip += 2
        case 7:
            regs[2] = regs[0] >> combo
            ip += 2

print(','.join(map(str, out)))
