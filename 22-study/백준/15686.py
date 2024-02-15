# https://www.acmicpc.net/problem/15686

from itertools import combinations

N,M = map(int,input().split())
arr=[list(map(int,input().split())) for _ in range(N)]
chick = []
house = []
dist = int(1e9)

for i in range(N):
    for j in range(N):
        if arr[i][j] == 1:
            house.append((i,j))
        elif arr[i][j] == 2:
            chick.append((i,j))


for j in combinations(chick, M):
    total = 0
    for i in house:
        tmp = int(1e9)
        for k in j:
            #print(k)
            tmp = min(tmp, abs(k[0]-i[0])+abs(k[1]-i[1]))
            #print("chick",k[0],k[1])
            #print("house", i[0],i[1])
        total+=tmp
    dist = min(dist, total)
        
print(dist)