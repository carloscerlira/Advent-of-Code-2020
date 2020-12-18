import sys 
sys.stdin = open('input.txt', 'r')  
from collections import defaultdict

def get_valid_tickets():
    m, n = len(tickets), len(tickets[0])
    def is_valid(num):
        for field in lookup:
            for a,b in lookup[field]:
                if a <= num <= b:
                    return True 
        return False 

    ans = 0
    valid_tickets = []
    for ticket in tickets:
        valid_ticket = True 
        for num in ticket:
            if not is_valid(num): 
                ans += num
                valid_ticket = False 
        if valid_ticket:
            valid_tickets.append(ticket)

    return valid_tickets

def solve():
    def get_fields(num):
        fields = set()
        for field in lookup:
            for a,b in lookup[field]:
                if a <= num <= b:
                    fields.add(field)
        return fields

    valid_tickets = get_valid_tickets()
    m, n = len(valid_tickets), len(valid_tickets[0])
    cols = [[valid_tickets[i][j] for i in range(m)] for j in range(n)]
    
    poss_fields = defaultdict(set)
    for j in range(n):
        col = cols[j]
        fields = get_fields(col[0])
        for num in col:
            fields = fields & get_fields(num)
        poss_fields[j] = fields
    
    def outer_left(A, B):
        return [a for a in A if a not in B]

    found = defaultdict(str)
    while len(found) != n:
        for j in range(n):
            field = poss_fields[j]
            for k in range(n):
                if k == j: continue 
                field = outer_left(field, poss_fields[k])
            if len(field) == 1:
                found[j] = list(field)[0]  
                del poss_fields[j]
    ans = 1
    for j in found:
        if "departure" in found[j]:
            ans *= mine[j]
    return ans 

lookup = defaultdict(list)
tickets = []
step = 0
while True:
    try: 
        line = input()
        if not line: 
            step += 1
            continue

        if step == 0:
            line = line.split(":")
            field = line[0]
            bounds = line[1].split("or")
            bounds = [x.strip() for x in bounds]
            for bound in bounds:
                a, b = map(int, bound.split("-"))
                lookup[field].append((a, b))
        
        if step == 1:
            if line == "your ticket:": continue
            mine = list(map(int, line.split(",")))
            
        if step == 2:
            if line == "nearby tickets:": continue 
            ticket = list(map(int, line.split(",")))
            tickets.append(ticket)            
    except:
        break
print(solve())
