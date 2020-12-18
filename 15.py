import sys 
sys.stdin = open('input.txt', 'r')  
from collections import defaultdict
def solve(arr):
    n = len(arr)
    spoken = defaultdict(lambda: (None, None))
    for i in range(n):
        spoken[arr[i]] = (i, None)

    last = arr[-1] 
    for i in range(n, 30_000_000):
        if last in spoken:
            first, second = spoken[last]
            if second != None: 
                last = second-first
            else: 
                last = 0
        
            first, second = spoken[last]
            if first == None: 
                first = i 
            elif second == None: 
                second = i
            else: 
                first, second = second, i  
            spoken[last] = (first, second) 
        else:
            last = 0 
    return last 

while True:
    try: 
        line = input()
        arr = [int(x) for x in line if x != ","]
    except:
        break
print(solve(arr))