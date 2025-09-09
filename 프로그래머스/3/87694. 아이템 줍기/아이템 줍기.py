from collections import deque
from math import ceil

def solution(rectangles, characterX, characterY, itemX, itemY):
    [characterX, characterY, itemX, itemY]=[characterX*2, characterY*2, itemX*2, itemY*2]
    
    ### 기존 도화지 (0)
    graph = [[0 for _ in range(102)] for _ in range(102)]
    answer = 0
    ### 영역 싹다 색칠하기 (1)
    for rectangle in rectangles:
        x1,y1,x2,y2 = rectangle
        for y in range(y1*2, y2*2+1):
            for x in range(x1*2,x2*2+1):
                graph[y][x]=1

    ### 영역 안쪽 색칠 벗기기 (0)
    for rectangle in rectangles:
        [x1,y1,x2,y2] = rectangle
        for y in range(y1*2+1, y2*2):
            for x in range(x1*2+1,x2*2):
                graph[y][x]=0
    ### 1인 곳만 이동 가능하게 하기 (나중에 이동 횟수는 나누기 2)
    directions = [[0,-1],[0,1],[1,0],[-1,0]]
    que = deque()
    que.append([characterY, characterX])
    while(que):
        y,x = que.popleft()
        ##print(y,x)
        if(y==itemY and x==itemX):
            answer = (graph[y][x]//2)
            break
        for dx,dy in directions:
            nx, ny = dx+x, dy+y
            if(not(0<=nx<102) or not(0<=ny<102) or graph[ny][nx]!=1):
                continue
            graph[ny][nx] = graph[y][x]+1
            que.append([ny, nx])

    return answer