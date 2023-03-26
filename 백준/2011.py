import sys
input=sys.stdin.readline
code = [0]+list(map(int,input().strip()))
l = len(code)
dp = [0]*(l)
dp[0],dp[1]=1,1


def solution():
    if code[1]==0:
        return 0
    else:
        for i in range(2, l):
            first = int(code[i])
            tenth = int(code[i-1])*10 + int(code[i])
            if first > 0: 
                dp[i] += dp[i-1]
            if tenth >= 10 and tenth <= 26: dp[i] += dp[i-2]
        return dp[-1]%1000000

print(solution())