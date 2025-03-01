import sys
input = sys.stdin.readline
from collections import deque

n = int(input())
arr = list(map(int, input().split()))
ROW = max(arr[0],arr[2])+1
COL = max(arr[1],arr[3])+1
INF = float("inf")
distance  = [[INF for _ in range(COL)] for _ in range(ROW)]

directions = [
    [-2,-1],[-2,+1],
    [0,-2],[0,2],
    [2,-1],[2,1]
]

# print(distance)
# print(arr, n, ROW, COL)


def bfs(r,c):
    que = deque()
    que.append([r,c])
    distance[r][c] = 0
    while (que):
        r,c = que.popleft()
        if((r==arr[2]) and (c==arr[3])):
            break
        for [dr,dc] in directions:
            nr, nc = r+dr, c+dc
            
            ## 범위 안 아니면 종료
            if(not(0<=nr<ROW) or not(0<=nc<COL) or distance[nr][nc]!=INF):
                continue

            distance[nr][nc] = distance[r][c]+1
            que.append([nr, nc])

            
bfs(arr[0],arr[1])
answer = -1 if distance[arr[2]][arr[3]]==INF else distance[arr[2]][arr[3]]
print(answer)