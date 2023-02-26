import sys
input = sys.stdin.readline

n,m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
dx=[1,-1,0,0]
dy=[0,0,1,-1]
visited = [[False]*m for _ in range(n)]
max_pos = max(map(max, arr))
ans = 0

def dfs(x, y, step, total):
    global ans
    if ans>=total+max_pos*(3-step):
        return 
    if step == 3:
        ans = max(ans, total)
    else:
        for i in range(4):
            nx, ny = x + dx[i], y+dy[i]
            if 0<=nx<n and 0<=ny<m and not visited[nx][ny]:
                if step==1:
                    visited[nx][ny]=True
                    dfs(x,y,step+1,total+arr[nx][ny])
                    visited[nx][ny]=False
                visited[nx][ny]=True
                dfs(nx,ny,step+1,total+arr[nx][ny])
                visited[nx][ny]=False




for x in range(len(arr)):
    for y in range(len(arr[x])):
        visited[x][y]=True
        dfs(x,y,0, arr[x][y])
        visited[x][y]=False

print(ans)