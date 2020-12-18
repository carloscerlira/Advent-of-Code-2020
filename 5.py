def solve(arr):
    def get_id(pattern, l, r, letter):
        n = len(pattern)
        i = 0
        while i < n and l <= r:
            mid = l+(r-l)//2
            if pattern[i] == letter:
                r = mid-1
                i += 1
            else:
                l = mid+1
                i += 1
        return l

    ans = -1
    seats = set()
    for pattern in arr:
        row = get_id(pattern, 0, 127, "F")
        col = get_id(pattern[-3:], 0, 7, "L")
        seats.add((row, col))
        idx = row*8+col 
        ans = max(ans, idx)

    for row in range(1, 127):
        for col in range(0, 7+1):
            if (row, col) not in seats:
                print(row*8+col)
    
    return

# arr = ["FBFBBFFRLR", "BFFFBBFRRR", "FFFBBBFRRR", "BBFFBBFRLL"]
# print(solve(arr))  
arr = []
x = input()
while x:
    try:
        arr.append(x)
        x = input()
    except ValueError:
        break

print(solve(arr))