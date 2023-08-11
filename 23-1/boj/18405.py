import sys
from collections import deque
from copy import deepcopy
input = sys.stdin.readline

# n: 그래프 row, k: 바이러스 종류 갯수
n,k=map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
s,x,y = map(int, input().split())

dr = [-1,1,0,0]
dc = [0,0,-1,1]

virus = []
que = deque()
t_que = deque()

for i in range(n):
    for j in range(n):
        if graph[i][j]!=0:
            virus.append([i,j, graph[i][j]])
            
virus.sort(key = lambda x : x[2])

for r,c,v in virus:
    que.append([r,c])
            
def bfs(s, que):
    count=1
    while que:
        if count>s:
                return
        r,c = que.popleft()
        for idx in range(4):
            nr, nc = r + dr[idx], c+ dc[idx]
            if not(0<=nr<n and 0<=nc<n):
                continue
            if graph[nr][nc]==0:
                graph[nr][nc] = graph[r][c]
                t_que.append([nr, nc])
        #print("##",count,"##")
        #for i in graph:
        #    print(i)       
        #print("####")
        if len(que)==0:
            count+=1
            que = deepcopy(t_que)
            t_que.clear()
            
            
bfs(s, que)
print(graph[x-1][y-1])