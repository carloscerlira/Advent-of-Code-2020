import sys 
sys.stdin = open('input.txt', 'r')  
from collections import defaultdict
from itertools import product

def solve(mat):
    def get_val(x,y,z,w):
        active = 0 
        for dw, dz, dx, dy in product([-1,0,1], repeat=4):
            if dx == dy == dz == 0 == dw: continue
            nx, ny, nz, nw = x+dx, y+dy, z+dz, w+dw 
            if not (0 <= nx < m and 0 <= ny < n and 0 <= nz < r and 0 <= nw < l): continue   
            if mat[nw][nz][nx][ny] == "#": active += 1

        curr = mat[w][z][x][y] if (0 <= x < m and 0 <= y < n and 0 <= z < r and  0 <= w < l) else ","
        if curr == "#": 
            if active == 2 or active == 3: return "#"
            else: return "."
        else:
            if active == 3: return "#"
            else: return "." 
              
    l, r, m, n = 1, 1, len(mat), len(mat[0])
    mat = [[[[mat[x][y] for y in range(n)] for x in range(m)] for z in range(r)] for w in range(l)]

    for cycle in range(6):
        l, r, m, n = len(mat), len(mat[0]), len(mat[0][0]), len(mat[0][0][0])
        new_mat = [[[["," for y in range(n+2)] for x in range(m+2)] for z in range(r+2)] for w in range(l+2)]
        for w, z, x, y in product(range(l+2), range(r+2), range(m+2), range(n+2)):
            new_mat[w][z][x][y] = get_val(x-1,y-1,z-1,w-1)
        mat = new_mat
    
    l, r, m, n = len(mat), len(mat[0]), len(mat[0][0]), len(mat[0][0][0])
    active = 0    
    for w, z, x, y in product(range(l), range(r), range(n), range(m)):
        if mat[w][z][x][y] == "#": active += 1
    return active 

mat = []
while True:
    try: 
        line = input()
        mat.append([x for x in line])
    except:
        break
print(solve(mat))
