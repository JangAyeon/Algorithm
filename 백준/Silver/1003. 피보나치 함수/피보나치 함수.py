
import sys

T = int(input())
m=80
dp = [[0,0] for _ in range(m)]
dp[0]=[1,0]
dp[1]=[0,1]



    
arr=[]
for _ in range(T):
    arr.append(int(input()))

n = max(arr)
for i in range(2,n+1):
    a,b = (dp[i-1])
    c,d = dp[i-2]
    dp[i]=[a+c,b+d]

for i in arr:
    print(*dp[i])
