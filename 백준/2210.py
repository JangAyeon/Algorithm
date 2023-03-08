import sys
input = sys.stdin.readline
from collections import deque

arr = [list(map(str, input().split())) for _ in range(5)]
dx = [1,-1,0,0]
dy = [0,0,1,-1]
res = []



def dfs(x,y,number):
    if len(number)==6:
        if number not in res:
            res.append(number)
        return
    
    for i in range(4):
        nx , ny = x + dx[i], y + dy[i]
        if 0 <= nx < 5 and 0 <= ny < 5: #범위 내에 있다면
            dfs(nx, ny, number + arr[nx][ny]) #6글자가 될 때 까지 재귀

for i in range(5):
    for j in range(5):
        dfs(i,j,arr[i][j])

print(res)