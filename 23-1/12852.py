import sys
input = sys.stdin.readline

N = int(input())
dp = [[0,0]]*(N+1) 

def getDP(N):

    for i in range(2, N+1):
        dp[i] = [dp[i-1][0]+1, i-1]
        if(i%3==0 and dp[i][0]>dp[i//3][0]+1):
            dp[i] = [dp[i//3][0]+1, i//3]
        if(i%2==0 and dp[i][0]>dp[i//2][0]+1):
            dp[i] = [dp[i//2][0]+1, i//2]
    return dp
    
def solution(N):
    dp = getDP(N)
    result = [0,[]]
    result[0] = dp[N][0]
    
    tmp = N
    while tmp!=0:
        result[1].append(tmp)
        tmp=dp[tmp][1]
    return result

answer = solution(N)
print(answer[0])
print(*answer[1])