import sys
input = sys.stdin.readline

n,m=map(int, input().split())

graph = [list(map(int, input().split())) for _ in range(n)]
sumDp = [[0]*(n+1) for _ in range(n+1)]

for row in range(1,n+1):
    for col in range(1, n+1):
        number = graph[row-1][col-1]
        sumDp[row][col] = sumDp[row][col-1]+sumDp[row-1][col]-sumDp[row-1][col-1]+number
        
        
for _ in range(m):
    x1,y1,x2,y2 = map(int, input().split())
    answer =sumDp[x2][y2] -(sumDp[x1-1][y2]+sumDp[x2][y1-1]-sumDp[x1-1][y1-1])
    print(answer)