import re 
import sys 
sys.stdin = open('input.txt', 'r')  
# sys.stdin = open('example.txt', 'r')  

def solve(eqs):
    def solve(eq):
        n = len(eq)
        op, res = None, None 
        i = 0 
        while i < n:
            if eq[i].isdigit():
                b = int(eq[i])
                res = res+b if res else b      
            elif eq[i] == "(":
                j, cnt = i+1, 1
                while cnt:
                    if eq[j] == "(": cnt += 1
                    if eq[j] == ")": cnt -=1 
                    j += 1
                b = solve(eq[i+1:j])
                res = res+b if res else b      
                i = j+1
                continue 
            elif eq[i] == "*":
                return res*solve(eq[i+1:])        
            i += 1
        return res
    return sum([solve(eq) for eq in eqs])

eqs = []
while True:
    try: 
        line = input()
        eqs.append(line)
    except:
        break
print(solve(eqs))
