import sys
input = sys.stdin.readline

n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]

area = {0:0,1:0}
def divided(r,c,n):
    curr = graph[r][c]
    for i in range(r,r+n):
        for j in range(c, c+n):
            if curr!=graph[i][j]:
                gap = n//2
                divided(r,c, gap)
                divided(r,c+gap, gap)
                divided(r+gap, c, gap)
                divided(r+gap, c+gap, gap)
                return
            
    area[curr]+=1
    return

divided(0,0,n)
for i in area.values():
    print(i)