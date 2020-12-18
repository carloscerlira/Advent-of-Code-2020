def solve():
    n = len(opts)
    def terminates():  
        seen = set()
        accumulator = 0
        i = 0 
        while i < n:
            if i in seen:
                return None
            seen.add(i)
            op, num = opts[i]
            if op == "nop":
                pass 
            elif op == "acc":
                accumulator += num
            else:
                i += num
                continue 
            i += 1 
        return accumulator 
    
    for i in range(n):
        op, num = opts[i]
        if op == "nop":
            opts[i] = ("jmp", num)
            accumulator = terminates()
            if accumulator: return accumulator
            opts[i] =  ("nop", num)
        if op == "jmp":
            opts[i] = ("nop", num)
            accumulator = terminates()
            if accumulator: return accumulator
            opts[i] = ("jmp", num)
    return -1 
    
opts = []
line = input()
while line:
    op, val = line.split(" ")
    sign = 1 if val[0] == "+" else -1
    num = sign*int(val[1:])
    opts.append((op, num))
    line = input()

print(solve())