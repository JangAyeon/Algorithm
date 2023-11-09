T = int(input())
for idx in range(T):
    n = int(input())    
    arr = [[] for _ in range(n)]
    arr[0]=[1]

    for i in range(1,n):
        for j in range(0,i+1):
            if j==0 or j==i:
                arr[i].append(1)
            else:
                arr[i].append(arr[i-1][j-1]+arr[i-1][j])
                
    print('#{0}'.format(idx+1))
    for row in arr:
        print(*row)
