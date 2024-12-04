input = [ l.strip() for l in open(0) ]

def search(x, y, dx, dy, s, input):
    ox, oy = x, y
    for c in s:
        if not (0 <= y < len(input) and 0 <= x < len(input[y])):
            return 0
        if input[y][x] != c:
            return 0
        x += dx
        y += dy
    return 1

r = 0
xmas = 'XMAS'
d = [-1, 0, 1]
for y, row in enumerate(input):
    for x, _ in enumerate(row):
        for dx in d:
            for dy in d:
                r += search(x, y, dx, dy, xmas, input)
print(r)