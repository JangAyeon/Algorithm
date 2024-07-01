import sys
input = sys.stdin.readline

n,m =map(int, input().split())
arr = [0]+list(map(int, input().split()))
## print(n,m,arr)

#0번 제거, 1번 제거, 2번 제거, m번 제거
dp = [[0 for _ in range(m+1)] for _ in range(n+1)]

for i in range(1,n+1):
    s = arr[i]%2 
    for j in range(m+1):
        if s==0: ## 짝수인 경우
            dp[i][j]=dp[i-1][j]+1
        else: ## 홀수인 경우
            if j==0:
                continue
            dp[i][j]=dp[i-1][j-1]

result = []               
for v in dp:
    result.append(v[m])
    
print(max(result))