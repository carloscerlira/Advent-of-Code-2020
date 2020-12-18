def solve(mat):
    def gen_new_mat(mat):
        def get_cnt(i, j): 
            def get_seat(i, j, dx, dy):
                i, j = i+dx, j+dy 
                while 0 <= i < m and 0 <= j < n:
                    if mat[i][j] != ".": return mat[i][j]
                    i, j = i+dx, j+dy
                return "."
            cnt = 0
            for dx in [-1, 0, 1]:
                for dy in [-1, 0, 1]:
                    if dx == 0 and dy == 0: continue 
                    if get_seat(i, j, dx, dy) == "#": cnt += 1
            return cnt
            
        new_mat = [[mat[i][j] for j in range(n)] for i in range(m)]
        for i in range(m):
            for j in range(n):
                if mat[i][j] == "L":
                    cnt = get_cnt(i,j)
                    if cnt == 0: new_mat[i][j] = "#"
                if mat[i][j] == "#":
                    cnt = get_cnt(i,j)
                    if cnt >= 5: new_mat[i][j] = "L"
        return new_mat 
    
    m, n = len(mat), len(mat[0])
    new_mat = gen_new_mat(mat)
    while new_mat != mat:
        mat = new_mat
        new_mat = gen_new_mat(mat)
    
    ans = 0
    for i in range(m):
        for j in range(n):
            if mat[i][j] == "#": ans += 1
    return ans 


mat = []
line = input()
while line:
    mat.append([char for char in line])
    line = input()
print(solve(mat))