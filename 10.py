from collections import defaultdict
from functools import lru_cache
def find_mult():
    n = len(nums)
    lookup = defaultdict(int)
    nums.sort()
    for i in range(1, n):
        lookup[abs(nums[i]-nums[i-1])] += 1
    return lookup[1]*lookup[3]

def find_ways():
    n = len(nums)
    nums.sort()
    @lru_cache(None)
    def dp(i):
        if i == n-1: return 1
        ways = 0
        for k in range(i+1, i+3+1):
            if k >= n: continue
            if abs(nums[k]-nums[i]) <= 3:
                ways += dp(k)
        return ways 
    return dp(0)


nums = []
num = input()
while num:
    nums.append(int(num))
    num = input()
nums.append(0)
nums.append(max(nums)+3)
print(find_mult())