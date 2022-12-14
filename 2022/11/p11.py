def read_monkeys(file='input.txt'):
    sections = open(file, 'rt').read().split('\n\n')
    for l in sections:
        l = l.splitlines()
        res = {}
        # items
        res['items'] = list(map(int, l[1].split(':')[1].split(',')))
        # operation
        op = l[2].split('=')[1]
        res['op'] = eval('lambda old: ' + op)
        # div
        res['div'] = int(l[3].split()[3])
        res['true'] = int(l[4].split()[5])
        res['false'] = int(l[5].split()[5])
        yield res

def p1(normalize = lambda item: item // 3, rounds=20):
    monkeys = []
    for monkey in read_monkeys():
        monkeys += [monkey]
    inspections = [0] * len(monkeys)
    for i in range(0, rounds):
        for id, m in enumerate(monkeys):
            for item in m['items']:
                inspections[id] += 1
                item = m['op'](item)
                item = normalize(item)
                idx = m['true'] if item % m['div'] == 0 else m['false']
                monkeys[idx]['items'].append(item)
            m['items'] = []
    inspections.sort()
    print(inspections)
    print(inspections[-1] * inspections[-2])

def p2():
    monkeys = []
    mod = 1
    for monkey in read_monkeys():
        monkeys += [monkey]
        mod *= monkey['div']
    p1(normalize = lambda x, m=mod: x % m, rounds=10000)

p1()
p2()