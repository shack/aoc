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
    print(ox, oy, dx, dy)
    return 1

r = 0
for y, row in enumerate(input):
    for x, c in enumerate(row):
        if c == 'A':
            a = search(x - 1, y - 1, 1, 1, 'MAS', input)
            b = search(x - 1, y - 1, 1, 1, 'SAM', input)
            c = search(x - 1, y + 1, 1, -1, 'MAS', input)
            d = search(x - 1, y + 1, 1, -1, 'SAM', input)
            if a + b == 1 and c + d == 1:
                r += 1
print(r)