input = [ l.strip() for l in open(0) ]

def match(s):
    l = len(s)
    for i in range(1, l + 1):
        w = l // i
        if w > 1 and w * i == l and s == s[:i] * w:
            return True
    return False

res = 0
for l in input:
    for pair in l.split(','):
        l, u = pair.split('-')
        for i in range(int(l), int(u)+1):
            s = str(i)
            if match(s):
                res += i
print(res)