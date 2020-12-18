from collections import Counter
ans = 0
while True: 
    line = input()
    cnt = Counter()
    n = 0
    while line != "":
        n += 1
        for x in line:
            cnt[x] += 1
        line = input()
    for x in cnt:
        if cnt[x] == n: ans += 1
    if line == "0": break  
print(ans)
