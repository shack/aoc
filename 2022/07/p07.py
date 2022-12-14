def input(name='input.txt'):
    with open(name, 'rt') as f:
        for l in f:
            yield l.rstrip()

def gen_tree():
    tree = cwd = { '/': {} }
    for l in input():
        cmds = l.split(' ')
        if cmds[0] == '$':
            cmd = cmds[1]
            if cmd == 'cd':
                dir = cmds[2]
                if dir == '..':
                    cwd = cwd['..']
                else:
                    if dir != '/':
                        cwd[dir]['..'] = cwd
                    cwd = cwd[dir]
            elif cmd == 'ls':
                pass
        else:
            c = l.split(' ')
            if c[0] == 'dir':
                cwd[c[1]] = {}
            else:
                cwd[c[1]] = int(c[0])
    return tree

def recurse(dir, f):
    sum = 0
    for k in dir:
        if k == '..':
            pass
        elif type(dir[k]) is dict:
            s = recurse(dir[k], f)
            sum = sum + s
        else:
            sum = sum + dir[k]
    f(sum)
    return sum

def p1():
    tree = gen_tree()
    total = 0

    def total_sum(sum):
        nonlocal total
        if sum <= 100000:
            total = total + sum

    recurse(tree, total_sum)
    print(total)

def p2():
    tree = gen_tree()
    required = 0
    curr_min = 0

    def find_min(sum):
        nonlocal required
        nonlocal curr_min
        if sum >= required and sum < curr_min:
            curr_min = sum
    
    def empty(sum):
        pass
    
    overall = recurse(tree, empty)
    required = overall - 40000000
    curr_min = overall
    recurse(tree, find_min)
    print(curr_min)

p1()
p2()