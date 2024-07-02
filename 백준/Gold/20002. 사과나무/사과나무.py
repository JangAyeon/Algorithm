import sys
input = sys.stdin.readline

n = int(input())
graph = [[0 for _ in range(n+1)]]


for _ in range(n):
    row = [0]+list(map(int, input().split()))
    graph.append(row)

for i in range(1,n+1):
    for j in range(1,n+1):
        graph[i][j]+=graph[i-1][j]+graph[i][j-1]-graph[i-1][j-1]



answer = graph[1][1]
for size in range(1,n+1):
    for i in range(size,n+1):
        for j in range(size,n+1):
            result = graph[i][j]-graph[i-size][j]-graph[i][j-size]+ graph[i-size][j-size]
            ###print(size,(i,j),result )
            answer=max(answer, result)

print(answer)