T = 10

for i in range(T):


    n = int(input())
    arr = list(map(int, input().split()))
    
    ans = []
    for idx, height in enumerate(arr[2:-2],2):
        temp = 256
        for dx in [-1,1,-2,2]:
            if arr[idx+dx]<height:
                temp = min(temp, height-arr[idx+dx])
            else:
                temp = 0
                break
        ans.append(temp)
    print('#{0} {1}'.format(i+1, sum(ans)))