# 백준 루머
# https://www.acmicpc.net/problem/19538



import sys
input = sys.stdin.readline
from collections import deque



n = int(input().strip())
graph = [0]
for _ in range(n):
    *a, b =map(int, input().split())
    graph.append(a)
m = int(input().strip())
start = list(map(int,input().split()))
#print(graph, start)

visited = [0]*(n+1)
cnt = [0]*(n+1)
ans = [-1]*(n+1)
que = deque()

for i in start:
    que.append(i)
    ans[i]=0
    visited[i]=1


def bfs():
    while que:
        current = que.popleft()
        for next in graph[current]:
            if not visited[next]:
                cnt[next]+=1
                if cnt[next]>=(len(graph[next])+1)//2:
                    ans[next]=ans[current]+1
                    que.append(next)
                    visited[next]=1

bfs()
print(*ans[1:])