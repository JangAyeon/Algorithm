import sys
input = sys.stdin.readline
from collections import deque



BEER = 20
DISTANCE_CHUNK=50


def bfs(startR,startC, endR, endC):
    que= deque()
    que.append([startR,startC])
    while que:
        currR,currC= que.popleft() # 현재 위치
        dist = abs(currR-endR)+abs(currC-endC)
        if (dist<=DISTANCE_CHUNK*BEER): ## 해당 위치에서 콘서트장까지 갈 수 있음
            #print(r,c,b)
            return "happy"
        for idx in range(cnt):
            if visited[idx]:
                continue
            nextR, nextC =stores[idx]
            dist = abs(currR-nextR)+abs(currC-nextC)
            if (dist<=DISTANCE_CHUNK*BEER):
                visited[idx]=True
                que.append([nextR, nextC])
            
    return "sad"

T = int(input())

for _ in range(T):

    cnt = int(input())
    startR, startC = map(int, input().split())
    stores = []
    visited = []
    for _ in range(cnt):
        storeR, storeC = map(int, input().split())
        stores.append([storeR,storeC])
        visited.append(False)
    endR,endC = map(int, input().split())

    print(bfs(startR, startC, endR, endC))


        



"""
1

2

0 0

1000 5

2000 10

3000 15

answer : sad

"""