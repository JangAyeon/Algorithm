import sys
input = sys.stdin.readline

n,m = map(int, input().split())
r,c,d =  map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
dr = [-1,0,1,0]
dc = [0,1,0,-1]

graph[r][c]=-1
count=1

while graph[r][c]!=1:
    flag = False
    for _ in range(4):
        d = (d+3)%4
        nr,nc = r + dr[d],c+dc[d]
        if graph[nr][nc]==0:
            graph[nr][nc]=-1
            flag=True
            r=nr
            c=nc
            count+=1
            break
    if not flag:
        r,c = r + dr[d-2], c + dc[d-2]

print(count)