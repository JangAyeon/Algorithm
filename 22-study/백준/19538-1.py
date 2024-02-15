#https://www.acmicpc.net/source/49341332

import sys
input=sys.stdin.readline

from collections import deque
que = deque()

n = int(input())
graph = [[0]]
for _ in range(n):
    *a, b = list(map(int, input().split()))
    graph.append(a)

m = int(input())
start = list(map(int, input().split()))




#print(m,start, n, graph)
#print(ans, turn)
ans = [-1] * (n+1)
turn = [0]*(n+1)
for i in start:
    que.append(i)
    ans[i]=0
    

for i in range(1,n+1):
    turn[i] = (len(graph[i])+1) //2

def bfs():
    while que:
        current = que.popleft()
        for next in graph[current]:
            #print(turn[next],next)
            turn[next]-=1
            if ans[next]==-1 and turn[next]==0:
                que.append(next)
                ans[next] = ans[current]+1
                
    return ans[1:]
                
#print(ans)
print(*bfs())

