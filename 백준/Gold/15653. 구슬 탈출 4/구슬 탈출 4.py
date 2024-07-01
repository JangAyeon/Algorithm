import sys
input = sys.stdin.readline
from collections import deque

n,m = map(int, input().split())
graph=[]
r_start = []
b_start = []
visited=[[[[False for _ in range(m)]for _ in range(n)] for _ in range(m)] for _ in range(n)]
directions  = [[-1,0],[1,0],[0,1],[0,-1]]


for i in range(n):
    row = list(input().strip())
    if "R" in row:
        r_start = [i, row.index("R")]
    if "B" in row:
        b_start = [i, row.index("B")]
    graph.append(row)

##print(r_start, b_start)


def bfs(rr, rc, br,bc):
    que=deque()
    que.append([rr, rc, br, bc,0])
    visited[rr][rc][br][bc]=True
    while que:
        rr, rc,br,bc,count=que.popleft()
        
        if graph[rr][rc]=="O":
            return count
        for dr, dc in directions:
            nrr, nrc, nbr, nbc = rr, rc,br,bc
            while True:
                nrr+=dr
                nrc+=dc
                if graph[nrr][nrc]=="O":
                    break
                if graph[nrr][nrc]=="#":
                    nrr-=dr
                    nrc-=dc
                    break
            while True:
                nbr+=dr
                nbc+=dc
                if graph[nbr][nbc]=="O":
                    break
                if graph[nbr][nbc]=="#":
                    nbr-=dr
                    nbc-=dc
                    break
            if graph[nbr][nbc]=="O":
                continue
            if (nrr==nbr) and (nrc==nbc):
                if abs(rr-nrr)+abs(rc-nrc)>abs(br-nbr)+abs(bc-nbc):
                    nrr-=dr
                    nrc-=dc
                else:
                    nbr-=dr
                    nbc-=dc
            if not(visited[nrr][nrc][nbr][nbc]):
                que.append([nrr, nrc, nbr,nbc,count+1])
                visited[nrr][nrc][nbr][nbc]=True
    return -1


print(bfs(r_start[0], r_start[1], b_start[0],b_start[1]))