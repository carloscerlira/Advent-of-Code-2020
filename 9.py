from collections import defaultdict
def solve(premble):
    n = len(nums)
    def find_invalid():
        def valid(i):
            for k in range(i-premble, i):
                for j in range(i-premble, i):
                    if nums[k]+nums[j] == nums[i]: return True 
            return False 

        for i in range(premble, n):
            if not valid(i): return nums[i] 
        return -1 
    tar = find_invalid()
    lookup = defaultdict(int)
    pre = nums[0]
    for i in range(1, n):
        pre = pre+nums[i] 
        if pre-tar in lookup:
            j = lookup[pre-tar]
            break 
        if pre in lookup: continue
        lookup[pre] = i  

    smallest = nums[j]
    largest = nums[j]
    for k in range(j, i):
        smallest = min(smallest, nums[k])
        largest = max(largest, nums[k])
    
    return smallest+largest
        # x-y = k;
        # y = x-k
nums = []
num = input()
while num:
    nums.append(int(num))
    num = input()

print(solve(premble=25))