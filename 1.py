def solve(arr,k=2020):
    n = len(arr)
    lookup = set(arr)
    for i in range(n):
        for j in range(i, n):
            z = k-(arr[i]+arr[j])
            if z in lookup: 
                return arr[i]*arr[j]*z 
    
arr = []
while True:
    try:
        x = int(input())
        arr.append(x)
    except:
        break
    
print(solve(arr))