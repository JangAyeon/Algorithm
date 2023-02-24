import sys
input = sys.stdin.readline

N,M = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(N)]
visit = [[False]*M for _ in range(N)]
dx = [-1,1,0,0]
dy = [0,0,-1,1]
max_pos = max(map(max,arr)) 
res = 0

# ✨ DFS
def DFS(x,y,step,total):
    global res
    if res >= total + max_pos*(4-step):
        return # ✨ 예외처리
    if step == 4:
        res = max(res,total)
        return # ✨ 4칸을 돌면 == 테트로미노를 만들면
    else:
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<N and 0<=ny<M and not visit[nx][ny]:
                if step == 2: # ✨ 2번째 테트로미노에서
                    visit[nx][ny] = True
                    DFS(x,y,step+1,total+arr[nx][ny])
                    visit[nx][ny] = False
                visit[nx][ny] = True
                DFS(nx,ny,step+1,total+arr[nx][ny])
                visit[nx][ny] = False
            

for i in range(N):
    for j in range(M):
        visit[i][j] = True
        DFS(i,j,1,arr[i][j])
        visit[i][j] = False
print(res)