
def solution(n):
    dp = [0 for _ in range(n+1)]
    dp[2] =3
    
    for i in range(4, n+1,2):
        answer  = 0
        for j in range(2, i):
            if j+2 == i:
                answer+=3*dp[j]
            else:
                answer+=2*dp[j]
        dp[i]=answer+2
    
    
    return dp[n]%1000000007

