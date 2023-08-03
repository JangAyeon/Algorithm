import sys
input = sys.stdin.readline
n = int(input())
dp = [[0]*n for _ in range(n)]
arr = [list(map(int, input().split())) for _ in range(n)]
#print(n,dp, arr)
dp[0][0] = arr[0][0]

for i in range(1, n):
    for j in range(i):
        dp[i][j]=  max(dp[i][j],dp[i-1][j]+arr[i][j])
        dp[i][j+1]= max(dp[i][j+1],dp[i-1][j]+arr[i][j+1])
        #print(dp[i][j], dp[i][j+1])
        #print(dp)
        #print(i,j, arr[i][j])
        #print(i,j+1, arr[i][j+1])
    #print("=============")
        
print(max(dp[-1]))