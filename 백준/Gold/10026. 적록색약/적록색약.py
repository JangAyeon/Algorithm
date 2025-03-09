import sys
input = sys.stdin.readline
from collections import deque
N = int(input())
arr = [list(input().strip()) for _ in range(N)]


directions  = [
    [0, -1],[0,1],
    [1,0],[-1,0]
]
answer = [0, 0] ## 정상인, 적록 색맹

## 그냥 두번 돌려도 됨
def bfs(r,c, isSick): ## r, c, 적록색맹 여부 
    que = deque()
    color = arr[r][c]
    que.append([r,c]) ## r, c, type
    visited[r][c] = True
    while que:
        r,c = que.popleft()
        for [dr, dc] in directions:
            nr, nc = r+dr, c+dc
            if(not(0<=nr<N) or not(0<=nc<N) ) or visited[nr][nc]: ## 범위 나간 경우
                continue
             ## 적록 색맹인 경우
            if isSick == True and ((color=="B" and arr[nr][nc]=="B") or (color!="B" and arr[nr][nc]!="B")):
                    visited[nr][nc]=True
                    que.append([nr, nc])
            elif isSick==False and color == arr[nr][nc]:
                    visited[nr][nc]= True
                    que.append([nr, nc])

for idx in range(len(answer)):
    isSick = False if idx==0 else True
    visited = [[False for _ in range(N)] for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if not(visited[i][j]):
                answer[idx]+=1
                bfs(i, j , isSick)

print(*answer)