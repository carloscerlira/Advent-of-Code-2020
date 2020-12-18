import sys 
sys.stdin = open('input.txt', 'r')  
from itertools import combinations

def get_adresses(mask, val):
    n = len(mask)
    binary = bin(val)[2:]
    binary = "0"*(n-len(binary))+binary
    ans = []
    for i in range(n):
        if mask[i] == "0": 
            ans.append(binary[i])
        else:
            ans.append(mask[i])
    # ans = "".join(ans)
    indices = [i for i in range(n) if ans[i] == "X"]
    ans = [x if x != "X" else "0" for x in ans]
    adresses = []
    m = len(indices)
    for i in range(m+1):
        for comb in combinations(indices, i):
            temp = ans.copy()
            for idx in comb:
                temp[idx] = "1"
            temp = "".join(temp)
            adresses.append(int(temp, 2))
    return adresses 

# mask = "00000000000000000000000000000000X0XX"
# val = 26
# print(get_adresses(mask, val))
mem = {}
mask = None 
while True:
    try:
        line = input()
        line = line.split("=")
        line = [x.strip() for x in line]
        if line[0] == "mask":
            mask = line[1]
        else:
            adress, val = int(line[0][line[0].index("[")+1:-1]), int(line[1])
            # mem[key] = get_val(mask, val)
            adresses = get_adresses(mask, adress)
            for key in adresses:
                mem[key] = val
    except:
        break 
s = sum([mem[x] for x in mem])
# print(mem)
print(s)