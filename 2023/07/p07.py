import re
import sys
from functools import reduce, cmp_to_key
from collections import Counter

order = "AKQJT98765432"

def cmp_card(c1, c2):
    i1 = order.index(c1[0])
    i2 = order.index(c2[0])
    return i2 - i1

def cmp_hands_lex(h1, h2):
    for i in range(5):
        c = cmp_card(h1[i], h2[i])
        if c != 0:
            return c
    return 0

def type(hand):
    c = sorted(Counter(hand).values(), reverse=True)
    if c[0] == 5:
        return 6
    elif c[0] == 4:
        return 5
    elif c[0] == 3:
        return 4 if c[1] == 2 else 3
    elif c[0] == 2:
        return 2 if c[1] == 2 else 1
    elif c[0] == 1:
        return 0
    else:
        assert False

def cmp_hands(h1, h2):
    t1 = type(h1)
    t2 = type(h2)
    return t1 - t2 if t1 != t2 else cmp_hands_lex(h1, h2)

def p1():
    hands = { l.split()[0]: l.split()[1] for l in open(sys.argv[1], 'r') }
    sorted_hands = sorted(hands.keys(), key=cmp_to_key(cmp_hands))
    s = 0
    for i, h in enumerate(sorted_hands):
        s += (i + 1) * int(hands[h])
    print(s)

order = "AKQT98765432J"

def type_joker(hand):
    p = [ hand.replace('J', c) for c in set(hand) ]
    res = sorted(p, key=cmp_to_key(cmp_hands))
    return type(res[-1])

def cmp_hands_joker(h1, h2):
    t1 = type_joker(h1)
    t2 = type_joker(h2)
    return t1 - t2 if t1 != t2 else cmp_hands_lex(h1, h2)

def p2():
    hands = { l.split()[0]: l.split()[1] for l in open(sys.argv[1], 'r') }
    sorted_hands = sorted(hands.keys(), key=cmp_to_key(cmp_hands_joker))
    s = 0
    for i, h in enumerate(sorted_hands):
        s += (i + 1) * int(hands[h])
    print(s)

p1()
p2()


