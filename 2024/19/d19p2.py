from functools import cache

towels, patterns = open(0).read().split('\n\n')
towels = towels.split(', ')
patterns = patterns.split('\n')

@cache
def attempt(pattern):
    if len(pattern) == 0:
        return 1
    return sum(attempt(pattern[len(t):]) for t in towels if pattern.startswith(t))

print(sum(attempt(p) for p in patterns))