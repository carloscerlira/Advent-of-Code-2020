def solve():
    def get_cnt(l, r):
        cnt = 0
        m, n = len(arr), len(arr[0])
        i, j = 0, 0
        while i < m:
            i += l;
            j = (j+r)%n; 
            if i >= m and arr[i][j] == "#":
                cnt += 1
        return cnt 
    ans = 1
    for l, r in [[1, 1], [1, 3], [1, 5], [1, 7], [2, 1]]:
        ans *= get_cnt(l, r)
    print(ans)
    return 

arr = []
line = input()
while line:
    row = [x for x in line]
    arr.append(row)
    line = input()

solve()