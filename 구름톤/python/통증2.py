# day11: 통증(2)

import sys
input = sys.stdin.readline

n = int(input())
#print(n)
a,b = map(int, input().split())
INF = int(1e9)
# 이전 값, 연산 횟수
dp = [[INF,INF] for _ in range(n+1)]

# 테스트 케이스 3번, 4번 예외 처리 위해 필요
if a<n+1:
	dp[a]= [0,1]
if b<n+1:
	dp[b] = [0,1]

for i in range(a+1,n+1):
	if  dp[i-a]!=[INF,INF]:
		dp[i] = [i-a, dp[i-a][1]+1]
	if  dp[i-b]!=[INF,INF]:
		if dp[i][1]>dp[i-b][1]+1:
			dp[i] = [i-b, dp[i-b][1]+1]


if dp[-1][-1]==INF:
	print(-1)
else:
	print(dp[-1][-1])


"""
테스트 케이스 (3)
2
12 13
ans -1
"""

"""
테스트 케이스 (4)
2
2 3
ans -1
"""