input = [ l.strip() for l in open(0) ]

dial = 50
pw = 0
for line in input:
    dir = line[0]
    val = int(line[1:])
    match dir:
        case 'L':
            for i in range(val):
                dial = (dial - 1) % 100
        case 'R':
            for i in range(val):
                dial = (dial + 1) % 100
    if dial == 0:
        pw += 1
print(pw)
