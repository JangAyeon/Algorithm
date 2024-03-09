import sys
input = sys.stdin.readline

from collections import deque


def getGraph(l,r):
    graph=[]
    for _ in range(l):
        row =[]
        for _ in range(r):
            row.append(list(input().strip()))
        input()
        graph.append(row)
    return graph


def bfs(l,r,c):
    que = deque([[l,r,c,0]])
    visited[l][r][c]=True
    while que:
        l,r,c ,count= que.popleft()
        if graph[l][r][c]=="E":
            return "Escaped in "+str(count)+" minute(s)."
        for nl, nr, nc in [(l-1,r,c),(l+1,r,c),(l,r,c+1),(l,r,c-1),(l,r+1,c),(l,r-1,c)]:
            if not(0<=nl<L) or not(0<=nc<C) or not(0<=nr<R) or visited[nl][nr][nc]==True or graph[nl][nr][nc]=="#":
                continue
            visited[nl][nr][nc]=True
            que.append([nl, nr, nc, count+1])
    return "Trapped!"
    

while True:
    L,R,C =  map(int, input().split())
    if L==0:
        break
    graph = getGraph(L,R)
    visited = [[[False for _ in range(C)] for _ in range(R)] for _ in range(L)]

    for l in range(L):
        for r in range(R):
            for c in range(C):
                if graph[l][r][c]=="S":
                    print(bfs(l,r,c))