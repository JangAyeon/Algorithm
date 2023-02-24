# https://www.acmicpc.net/problem/12852

import sys
input = sys.stdin.readline

n = int(input())
dp = [[0,[]] for _ in range(n+1)]

# 1을 만드는 횟수, 방법
dp[1]=[0,[1]]

for i in range(2, n+1):
    dp[i]=[dp[i-1][0]+1, dp[i-1][1]+[i]]

    # 2로 나눠 떨어지는 경우
    if i % 2 == 0:
        if (dp[i][0]>dp[i//2][0]+1):
            dp[i] = [dp[i//2][0]+1, dp[i//2][1]+[i]] 

    if i % 3 == 0:
        if (dp[i][0]>dp[i//3][0]+1):
            dp[i] = [dp[i//3][0]+1, dp[i//3][1]+[i]] 

    # 3으로 나눠 떨어지는 경우
print(dp[n][0])
print(*dp[n][1][::-1])