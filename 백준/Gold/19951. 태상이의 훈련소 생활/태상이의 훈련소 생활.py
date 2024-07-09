import sys
input=sys.stdin.readline

n,m = map(int, input().split())
arr = list(map(int, input().split()))
dp=[0 for _ in range(n+2)]


for _ in range(m):
    a,b,deep = map(int, input().split())
    dp[a]+=deep
    dp[b+1]+=-deep



for i in range(1,n+2):
    dp[i]+=dp[i-1]



for i in range(n):
    arr[i]+=dp[i+1]
print(*arr)