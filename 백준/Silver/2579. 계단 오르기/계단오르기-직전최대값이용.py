import sys
input = sys.stdin.readline
n = int(input())
arr = [int(input()) for _ in range(n)]
dp = [0]*n

if n<3:
    if n==1:
        print(arr[-1])
    elif n==2:
        print(sum(arr))
else:
    dp[0] = arr[0]
    dp[1] = arr[0]+arr[1]
    for i in range(2,n):
        dp[i] = max(dp[i-2],dp[i-3]+arr[i-1])+arr[i]
    print(dp[-1])
