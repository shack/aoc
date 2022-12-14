def input(name='input.txt'):
    with open(name, 'rt') as f:
        for l in f:
            yield l.rstrip()

def all_different(last):
    return len(last) == len(set(last))

def search(n):
    for l in input():
        for i in range(n, len(l)):
            if all_different(l[i-n:i]):
                print(i)
                break

def p1():
    search(4)

def p2():
    search(14)

p1()
p2()