import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    n = int(input())
    dp = [[10-i for i in range(10)]]
    if n==1:
        print(10)
    else:
        for i in range(n-2):
            arr= []
            for j in range(10):
                arr.append(sum(dp[i][j:10]))
            dp.append(arr)
        print(sum(dp[-1]))