from collections import Counter
ans = 0
while True:
    try:
        line = input().split(" ")
        password = line[2]
        letter = line[1][0]
        idx1, idx2 = line[0].split("-")
        idx1, idx2 = int(idx1)-1, int(idx2)-1
        if password[idx1] == letter and password[idx2] != letter: ans += 1
        if password[idx2] == letter and password[idx1] != letter: ans += 1 
        print(ans)
    except ValueError:
        break