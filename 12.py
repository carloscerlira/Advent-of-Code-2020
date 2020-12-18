import math
def solve():
    x, y = 0, 0
    # wx, wy = 10, 1
    dx, dy = 10, 1 
    for op, val in opts:
        print(x, y)
        if op == "N":
            dy += val
        elif op == "S":
            dy -= val
        elif op == "E":
            dx += val
        elif op == "W":
            dx -= val
        elif op == "L":
            theta = val*math.pi/180 
            dx, dy = dx*math.cos(theta) - dy*math.sin(theta), dx*math.sin(theta)+dy*math.cos(theta)
        elif op == "R":
            theta = val*math.pi/180 
            dx, dy = dx*math.cos(-theta) - dy*math.sin(-theta), dx*math.sin(-theta)+dy*math.cos(-theta)
        elif op == "F":
            x += val*dx
            y += val*dy 
    # print(x,y)
    return abs(x)+abs(y)

# dx = 1
# dy = 0
# val = -90
# print(dx, dy)

opts = []
line = input()
while line:
    op, val = line[0], line[1:]
    op, val = op, int(val)
    opts.append((op, val))
    line = input()
print(solve())