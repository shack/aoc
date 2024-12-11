import sys

input = [ l.strip() for l in open(0) ][0]
input = [ int(i) for i in input.split() ]

def entries(i, max_level):
    visited = {}
    def rec(i, level):
        if (i, level) in visited:
            return visited[(i, level)]
        if level == max_level:
            res = 1
        elif i == 0:
            res = rec(1, level + 1)
        elif len(s := str(i)) % 2 == 0:
            h = len(s) // 2
            l, r = int(s[:h]), int(s[h:])
            res = rec(l, level + 1) + rec(r, level + 1)
        else:
            res = rec(i * 2024, level + 1)
        visited[(i, level)] = res
        return res
    return rec(i, 0)

max = int(sys.argv[1]) if len(sys.argv) > 1 else 25
print(sum(entries(i, max) for i in input))

