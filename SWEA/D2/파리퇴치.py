# https://swexpertacademy.com/main/code/problem/problemDetail.do


T = int(input())
for idx in range(T):
    n,m=map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(n)]
    ans = -1
    for startR in range(0,n):
        if startR+m<=n:
            rows = arr[startR:startR+m]
    
            for startC in range(0,n):
                temp=[]
                for row in rows:
                    if startC+m<=n:
                        temp.append(row[startC:startC+m])
                ans = max(ans,sum(sum(temp,[])))
    print('#{0} {1}'.format(idx+1, ans))
