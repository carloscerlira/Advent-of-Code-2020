import math 
def solve(times):
    n = len(times)
    # print(times)
    # min_wait = math.inf 
    # min_time = None
    # for idx, time in times:
    #     n, r = divmod(depart, time)
    #     if r: wait = time*(n+1)-depart 
    #     else: wait = time*n-depart
    #     if wait < min_wait:
    #         min_time = time 
    #         min_wait = wait
    # timestamp = 1068781
    # while True:
    #     valid = True 
    #     for i, time in times:
    #         n, r = divmod(timestamp, time)
    #         print(r, time-r, i)
    #         if time-r != i: valid = False
    #         # timestamp + i = n*time
    #         # timestamp = (n-1)*time + r = n*time - i
    #         # n*time - time + r = n*time - i 
    #         # -time + r = -i
    #         # time-r = i
    #         # r = time-i    
    #     if valid: return timestamp
    #     timestamp += 1 
    #     break 
    rem = [0]*n
    for i in range(1, n):
        pos, time = times[i]
        rem[i] = time-pos     
    return rem


# def findMinX(num, rem, k): 
#     x = 1; 
#     while(True): 
#         j = 0; 
#         while(j < k): 
#             if (x % num[j] != rem[j]): 
#                 break; 
#             j += 1; 
#         if (j == k): 
#             return x; 
#         x += 1; 

from functools import reduce
def chinese_remainder(n, a):
    sum = 0
    prod = reduce(lambda a, b: a*b, n)
    for n_i, a_i in zip(n, a):
        p = prod // n_i
        sum += a_i * mul_inv(p, n_i) * p
    return sum % prod
 
def mul_inv(a, b):
    b0 = b
    x0, x1 = 0, 1
    if b == 1: return 1
    while a > 1:
        q = a // b
        a, b = b, a%b
        x0, x1 = x1 - q * x0, x0
    if x1 < 0: x1 += b0
    return x1
  
depart = int(input())
line = input().split(",")
times = [(i, int(x)) for i, x in enumerate(line) if x != "x"]

nums = [x for i, x in times]
rem = solve(times)
print(chinese_remainder(nums, rem))

# print(findMinX(nums, rem, len(times)))