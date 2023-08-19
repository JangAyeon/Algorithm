import sys
input = sys.stdin.readline

n = int(input())

# 연산횟수, 이전 값
dp = [[0,0] for _ in range(n+1)]

for i in range(2,n+1):
    
    # 기본: 1 더하기로 i 만들기
    dp[i] = [dp[i-1][0]+1,i-1 ]
    
    # i가 3의 배수인 경우, 3 곱하기로 i 만들기
    if i%3==0 and dp[i][0]>dp[i//3][0]+1:
        dp[i] = [dp[i//3][0]+1, i//3]
        
    # i가 2의 배수인 경우, 2 곱하기로 i 만들기
    if i%2==0 and dp[i][0]>dp[i//2][0]+1:
        dp[i] = [dp[i//2][0]+1, i//2]
        


print(dp[-1][0])

idx = n
while idx !=0:
    print(idx, end=" ")
    idx = dp[idx][1]
    
