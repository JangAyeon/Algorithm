import sys
input=sys.stdin.readline
from collections import deque

dr=[-1,1,0,0]
dc = [0,0,-1,1]

n,m,c = map(int, input().split())
visited = [[False]*m for _ in range(n)]




    
def count(r,c):
    que = deque()
    que.append([r,c])
    visited[r][c]=True
    count=1
    while que:
        r,c, =que.popleft()
        for idx in range(4):
            nr, nc = r+dr[idx],c+dc[idx]
            if 0<=nr<n and 0<=nc<m and not(visited[nr][nc]):
                visited[nr][nc]=True
                que.append([nr, nc])
                count+=1
    return count
    
def area(startR, startC, endR, endC):
    for r in range(startR, endR):
        for c in range(startC, endC):
            visited[r][c]=True

for _ in range(c):
    startX, startY, endX, endY = map(int, input().split())
    endR,startC = (n)-startY, startX
    startR, endC = n-1-(endY-1),endX
    #print("## Area",startR, startC, endR, endC)
    area(startR, startC, endR, endC)
    

#for i in visited:
#    print(*i)   
ans=[]
for r in range(len(visited)):
    for c in range(len(visited[r])):
        if not(visited[r][c]):
            ans.append(count(r, c))


ans.sort()
print(len(ans))
print(*ans)