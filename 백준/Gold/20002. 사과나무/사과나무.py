import sys
input = sys.stdin.readline

n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]



preSum = [[0 for _ in range(n)] for _ in range(n)]

for i in range(n):
    for j in range(n):
        if i==0:
            if j==0:
                preSum[i][j]=graph[i][j]
            else:
                preSum[i][j]=preSum[i][j-1]+graph[i][j]
        else:
            if j==0:
                preSum[i][j]=preSum[i-1][j]+graph[i][j]
            else:
                preSum[i][j]=preSum[i-1][j]+preSum[i][j-1]-preSum[i-1][j-1]+graph[i][j]




answer= -1000
for size in range(1, n+1):
    for i in range(size-1, n):
        for j in range(size-1, n):
            temp = preSum[i][j]
            ##print("####",preSum[i][j])
            if i-size>=0:
                ##print(preSum[i-size][j], "빼기")
                temp-=preSum[i-size][j]
            if j-size>=0:
                ##print(preSum[i][j-size], "빼기")
                temp-=preSum[i][j-size]
            if i-size>=0 and j-size>=0:
                ##print(preSum[i-size][j-size], "더하기")
                temp+=preSum[i-size][j-size]
            ##print(size,(i,j), temp)
            answer=max(answer, temp)
print(answer)