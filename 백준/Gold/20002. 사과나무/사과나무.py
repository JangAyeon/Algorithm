import sys
input = sys.stdin.readline

n = int(input())
pre = [[-1001]*(n+1) for _ in range(n+1)]

# (i, j)까지의 구간합 구하기
for i in range(1, n+1):
    arr = list(map(int, input().split()))
    for j in range(1, n+1):
        pre[i][j] = pre[i][j-1] + pre[i-1][j] - pre[i-1][j-1] + arr[j-1]

max_profit = pre[0][0]
# 정사각형으로 자른다.
for k in range(n):
    for i in range(1, n-k+1):
        for j in range(1, n-k+1):
            # 시작점을 시작점(i, j), 끝점이(i+k, j+k)인 정사각형의 총이익
            profit = pre[i+k][j+k] - pre[i-1][j+k] - pre[i+k][j-1] + pre[i-1][j-1]
            max_profit = max(max_profit, profit)    # 최대 총이익 업데이트

print(max_profit)