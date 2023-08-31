import sys
input = sys.stdin.readline

arr = [list(map(str, input().split())) for _ in range(5)]
res = []
dx = [-1,1,0,0]
dy=[0,0,-1,1]


def dfs(x,y,number):
    if len(number)==6:
        if number not in res:
            res.append(number)
        return

    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if 0<=nx<5 and 0<=ny<5:
            dfs(nx, ny, number+arr[nx][ny])



for i in range(len(arr)):
    for j in range(len(arr[i])):
        dfs(i,j, arr[i][j])

print(len(res))