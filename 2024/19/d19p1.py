from functools import cache

towels, patterns = open(0).read().split('\n\n')
towels = towels.split(', ')
patterns = patterns.split('\n')

@cache
def attempt(pattern):
    if len(pattern) == 0:
        return True
    return any(attempt(pattern[len(t):]) for t in towels if pattern.startswith(t))

print(sum(1 for p in patterns if attempt(p)))