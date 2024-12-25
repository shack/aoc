items = open(0).read().split('\n\n')
items = [ item.split('\n') for item in items ]
keys = [ item for item in items if all(i == '#' for i in item[0]) ]
locks = [ item for item in items if all(i == '.' for i in item[0]) ]

def combine(k, l):
    for a, b in zip(k, l):
        for x, y in zip(a, b):
            if x == '#' and y == '#':
                return False
    return True

print(sum(combine(k, l) for k in keys for l in locks))