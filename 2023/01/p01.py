def p1():
    res = 0
    for l in open('input.txt', 'r'):
        q = l
        l = l.strip()
        for i in l:
            if i.isdigit():
                a = i
        l = l[::-1]
        for i in l:
            if i.isdigit():
                b = i
        num = int(b + a)
        res += num
    print(res)

def p2():
    res = 0
    names = [
        'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine'
    ]
    for l in open('input.txt', 'r'):
        pos = [ "" for i in l ]
        l = l.strip()
        for i in range(len(l)):
            for j, x in enumerate(names):
                if l[i:].startswith(x):
                    pos[i] = str(j + 1)
        for j, c in enumerate(l):
            if c.isdigit():
                pos[j] = c
        pos = [ s for s in pos if s != '' ]
        num = int(pos[0] + pos[-1])
        res += num
    print(res)

p1()
p2()


