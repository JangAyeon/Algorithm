import sys
input = sys.stdin.readline
from collections import deque

# 회원수
n = int(input())
INF = int(1e9)
graph =[[INF for _ in range(n+1)] for _ in range(n+1)]
for i in range(1, n+1):
    graph[i][i]=0

while True:
    a,b = map(int, input().split())
    if a==-1 and b==-1:
        break
    graph[a][b]=1
    graph[b][a]=1
    
# 플로이드 알고리즘
for mid in range(1, n+1):
    for start in range(1,n+1):
        for end in range(1, n+1):
            graph[start][end] = min(graph[start][end], graph[start][mid]+graph[mid][end])
                

score = INF
for i in range(1, n+1):
    score = min(score, max(graph[i][1:]))
team = []
for i in range(1, n+1):
    if score ==max(graph[i][1:]):
        team.append(i)
        
print(score, len(team))
print(*team)
