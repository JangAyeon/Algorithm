# 구슬탈출
import sys
from collections import deque
input = sys.stdin.readline
# 상하좌우
# UDLR
dir = {"L":[0,-1],"R":[0,1],"U":[-1,0],"D":[1,0]}
 
N, M = map(int, input().split())
visited = [[[[0 for i in range(M)] for i in range(N)] for i in range(M)] for i in range(N)]
 
graph = []
rStart =[]
bStart=[]
for r in range(N):
    tmp = list(input().strip())
    if "R" in tmp:
        rStart=[r, tmp.index("R")]
    if "B" in tmp:
        bStart = [r, tmp.index("B")]
    graph.append(tmp)

que = deque()
rr,rc = rStart
br,bc = bStart
que.append((rr,rc,br,bc, []))
 
visited[rr][rc][br][bc] = 1 # 방문처리
 
def bfs():
    while que:
        rr,rc,br,bc, route = que.popleft()
        
        if (len(route) > 10):
            print(-1)
            return
    
        if graph[rr][rc] == 'O':
            print(len(route))
            print("".join(route))
            return
        
        for d in dir.keys():
            # RED
            nrr, nrc = rr, rc
            while True:
                nrr += dir[d][0]
                nrc += dir[d][1]
                # 탈출조건1 - 벽
                if graph[nrr][nrc] == '#':
                    nrr -= dir[d][0]
                    nrc -=dir[d][1]
                    break
                # 탈출조건2 - 구멍
                if graph[nrr][nrc] == 'O':
                    break
            
            # BLUE
            nbr, nbc = br, bc
            while True:
                nbr += dir[d][0]
                nbc += dir[d][1]
                # 탈출조건1 - 벽
                if graph[nbr][nbc] == '#':
                    nbr -=dir[d][0]
                    nbc -=dir[d][1]
                    break
                # 탈출조건2 - 구멍
                if graph[nbr][nbc] == 'O':
                    break
            
            # Blue가 구멍에 들어가면 탐색할 가치가 없으므로
            if graph[nbr][nbc] == 'O': continue
            # BLUE와 RED가 같은 위치라면 더 멀리서 온 것을 뒤로 빼야한다.
            if (nrr == nbr and nrc == nbc):
                if( abs(nrr - rr) + abs(nrc - rc) > abs(nbr - br) + abs(nbc - bc) ):
                    nrr -= dir[d][0]
                    nrc -=dir[d][1]
                else:
                    nbr -= dir[d][0]
                    nbc -=dir[d][1]
            
            if visited[nrr][nrc][nbr][nbc] == 0:
                que.append((nrr, nrc, nbr, nbc, route+[d]))
                visited[nrr][nrc][nbr][nbc] = 1 # 방문처리    
    print(-1)
 
bfs()