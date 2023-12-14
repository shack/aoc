def transpose(input):
    return [ list(l) for l in zip(*input) ]

def tilt_west(input):
    return [ '#'.join([ ''.join(sorted(l)[::-1]) for l in ''.join(s).split('#') ]) for s in input ]

def tilt_north(input):
    return transpose(tilt_west(transpose(input)))

def tilt_south(input):
    return list(reversed(tilt_north(reversed(input))))

def tilt_east(input):
    rev = lambda l: list(reversed(l))
    return list(map(rev, tilt_west(map(rev, input))))


def weight(input):
    return sum((len(input) - i) * \
                sum(c == 'O' for c in l) for i, l in enumerate(input))

def map_to_str(input):
    return '\n'.join([''.join(l) for l in input])

def print_map(input):
    print('---\n', map_to_str(input))

def p1(input):
    print(weight(tilt_north(input)))

def cycle(input):
    input = tilt_north(input)
    input = tilt_west(input)
    input = tilt_south(input)
    input = tilt_east(input)
    return input

def p2(input):
    m = list(map(list, input))
    n = 1000000000
    seen = {}
    for i in range(1, n):
        input = cycle(input)
        s = map_to_str(input)
        if s in seen:
            start = seen[s]
            rest = (n - start) % (i - start)
            for i in range(rest):
                input = cycle(input)
            print(weight(input))
            return
        else:
            seen[s] = i

input = [ list(l.strip()) for l in open(0) ]

p1(input)
p2(input)