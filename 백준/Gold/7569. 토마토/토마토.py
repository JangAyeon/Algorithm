## 7569: 토마토


import sys
input = sys.stdin.readline
from collections import deque

C,R, F = map(int, input().split())
graph = [[list(map(int, input().split())) for _ in range(R)] for _ in range(F)]
visited = [[[False for _ in range(C)] for _ in range(R)] for _ in range(F)]

def bfs(starts):

    que=deque(starts)
    ## que.append([f,r,c])
    
    while que:
        f,r,c = que.popleft()
        visited[f][r][c]=True
        for nf, nr, nc in [(f-1,r,c),(f+1,r,c),(f,r-1,c),(f,r+1,c),(f,r,c+1),(f,r,c-1)]:
            ## 범위 나감
            ## print(nf, nr, nc)
            if not(0<=nf<F) or not(0<=nr<R) or not(0<=nc<C):
                ##print("범위 나감", nf, nr, nc)
                continue
            if  graph[nf][nr][nc]!=0:
                ##print("안 익은 토마토 아님", graph[nf][nr][nc])
                continue
            if  (visited[nf][nr][nc]):
                ##print("이미 방문함", nf, nr, nc, visited[nf][nr][nc])
                continue
            graph[nf][nr][nc] = graph[f][r][c]+1
            que.append([nf, nr, nc])
            visited[nf][nr][nc]=True


flag = False
starts = []
for f in range(F):
    for r in range(R):
        for c in  range(C):
            if graph[f][r][c]!=-1 and not(visited[f][r][c]):
                ## 토마토는 있음
                flag = True
                if graph[f][r][c]==1: ## 익은 토마토 있어서 번지기 가능
                    starts.append([f,r,c])

bfs(starts)

def getAnswer():
    answer = 0
    if not(flag): ## 이미 다 익어 있는 경우
        return 0
    else:
        for floor in graph:
            for r in floor:
                for e in r:
                    if e==0:
                        return -1
                    answer = max(answer, e)
        return answer-1

print(getAnswer())


"""
#문제의 조건대로 토마토가 있기는 한데, 그게 안익은 토마토라면?!
2 2 1
-1 -1
-1 0

ans : -1

3 2 1
0 0 0
0 0 1


ans: 3

2 2 2
1 -1
-1 0
-1 0
0 0

ans: -1

4 1 1
1 0 0 1
ans: 1
"""