import sys
input = sys.stdin.readline
from collections import deque

n,m = map(int, input().split())
rStart=[]
bStart=[]
graph=[]

visited = [[ [[ 0 for _ in range(m)]for _ in range(n)]for _ in range(m)]for _ in range(n)]
dir = {"L":[0,-1],"R":[0,1],"U":[-1,0],"D":[1,0]}


for r in range(n):
    lst = list(input().strip())
    if "R" in lst:
        rStart=[r, lst.index("R")]
    if  "B" in lst:
        bStart = [r, lst.index("B")]
    graph.append(lst)

def bfs():
    que = deque()
    rr,rc = rStart
    br,bc = bStart
    que.append([rr,rc,br,bc,[]])
    visited[rr][rc][br][bc]=1
    while que:
        rr,rc,br,bc,route = que.popleft()
        if len(route)>10:
            return [-1]
        if graph[rr][rc]=='O':
            return route
        for d in dir.keys():
            ## red
            nrr, nrc = rr,rc
            while True:
                nrr,nrc = nrr+dir[d][0], nrc+dir[d][1]
                if graph[nrr][nrc]=="#":
                    nrr,nrc = nrr-dir[d][0], nrc-dir[d][1]
                    break
                if graph[nrr][nrc]=='O':
                    break
                
            ## blue
            nbr, nbc = br,bc
            while True:
                nbr,nbc = nbr+dir[d][0], nbc+dir[d][1]
                if graph[nbr][nbc]=="#":
                    nbr,nbc = nbr-dir[d][0], nbc-dir[d][1]
                    break
                if graph[nbr][nbc]=='O':
                    break
                

            if graph[nbr][nbc]=='O':
                continue
            if nbr==nrr and nrc==nbc:
                ## red가 더 멀리서 온 경우
                if (abs(rr-nrr)+abs(rc-nrc))> (abs(br-nbr)+abs(bc-nbc)):
                    nrr , nrc= nrr-dir[d][0],nrc-dir[d][1]
                else:
                    nbr , nbc= nbr-dir[d][0],nbc-dir[d][1]


            if not(visited[nrr][nrc][nbr][nbc]):
                que.append([nrr,nrc,nbr,nbc,route+[d]])
                visited[nrr][nrc][nbr][nbc]=1
    return [-1]

answer = bfs()
if answer[-1]==-1:
    print(-1)
else:
    print(len(answer))
    print("".join(answer))