input = [ l.strip() for l in open(0) ]

res = 0
for l in input:
    for pair in l.split(','):
        l, u = pair.split('-')
        for i in range(int(l), int(u)+1):
            s = str(i)
            h = len(s) // 2
            if s[:h] == s[h:]:
                res += i
print(res)