import sys

nums = list(enumerate(map(int, sys.stdin.readlines())))

def mix(work, nums):
    for (idx, val) in nums:
        j = work.index((idx, val))
        work.pop(j)
        pos = (j + val) % len(work)
        if pos == 0:
            pos = len(work) 
        work.insert(pos, (idx, val))
    return [ v for _, v in work ]

work = nums[:]
res = mix(work, nums)
zero_idx = res.index(0)
print(sum(res[(zero_idx + i) % len(res)] for i in [1000, 2000, 3000]))

key = 811589153
nums = [ (i, v * key) for i, v in nums ]
work = nums[:]
for i in range(0, 10):
    res = mix(work, nums)
zero_idx = res.index(0)
print(sum(res[(zero_idx + i) % len(res)] for i in [1000, 2000, 3000]))