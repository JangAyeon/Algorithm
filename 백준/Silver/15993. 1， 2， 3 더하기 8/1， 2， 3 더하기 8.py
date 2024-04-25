import sys
input = sys.stdin.readline


## 홀, 짝

m= 1000000009
MAX =  100001
dp=[[0,0] for _ in range(MAX)]
dp[1] = [1,0]
dp[2]=[1,1]
dp[3]=[2,2]

for i in range(4,MAX):
    odd = (dp[i-1][1]+dp[i-2][1]+dp[i-3][1])%m
    even = (dp[i-1][0]+dp[i-2][0]+dp[i-3][0])%m
    dp[i] = [odd, even]
T = int(input())
for _ in range(T):
    n = int(input())
    print(*dp[n])