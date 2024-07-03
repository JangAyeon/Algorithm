import sys
input = sys.stdin.readline
n,m = map(int, input().split())

graph = [list(input().strip()) for _ in range(n)]

##print(graph)
move = n
dots = []

for c in range(m):
    snowR = -1
    blockR = n
    flag = False
    for r in range(n):
        ##print("##",r,c)
        if graph[r][c]=="X":
            flag = True
            dots.append([r,c])
            snowR = max(r, snowR)
        if graph[r][c]=="#":
            blockR = min(blockR,r)
    if flag:
        move = min(blockR-snowR-1, move)
    ##print(blockR,snowR,blockR-snowR-1)
move+=1
##print(move)




##print(dots)
dots.sort(reverse=True)
for r,c in dots:
    graph[r][c]="."
    graph[r+move-1][c]="X"


for i in graph:
    print("".join(i))