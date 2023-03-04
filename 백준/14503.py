# 참고 : https://resilient-923.tistory.com/164

import sys
input = sys.stdin.readline
"""
11 10
7 4 0
1 1 1 1 1 1 1 1 1 1
1 0 0 0 0 0 0 0 0 1
1 0 0 0 1 1 1 1 0 1
1 0 0 1 1 0 0 0 0 1
1 0 1 1 0 0 0 0 0 1
1 0 0 0 0 0 0 0 0 1
1 0 0 0 0 0 0 1 0 1
1 0 0 0 0 0 1 1 0 1
1 0 0 0 0 0 1 1 0 1
1 0 0 0 0 0 0 0 0 1
1 1 1 1 1 1 1 1 1 1
"""
n,m = map(int, input().split())
r,c,d = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]

visited = [[0]*m for _ in range(n)]
dr = [-1,0,1,0]
dc = [0,1,0,-1]

visited[r][c]=1
cnt=1

while True:
    flag = False
    for _ in range(4):
        d = (d+3)%4
        nr,nc = r + dr[d], c + dc[d]
        if 0<=nr<m and 0<=nc<n and not arr[nr][nc] and not visited[nr][nc]:
            visited[nr][nc]=1
            cnt+=1
            r=nr
            c=nc
            flag = True
            break
    if not flag:
        if arr[r-dr[d]][c-dc[d]]:
            print(cnt)
            break
        else:
            r,c = r-dr[d],c-dc[d]