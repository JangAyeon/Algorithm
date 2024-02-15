import sys
from collections import deque
input = sys.stdin.readline

row, col = map(int, input().split())
graph = [list(input().strip()) for _ in range(row)]

#print(row, col, graph)
answer=0


def isAble(r,c):
    if r<0 or c<0 or r>=row or c>=col:
        return False
    return True

def bfs(r, c):
    
    que = deque()
    que.append([r,c])
    
    while que:
        r,c =  que.popleft()
        if graph[r][c]=="-": # 양 옆에 조사
            graph[r][c] = 0 # 방문 처리
            for dc in [-1,1]:
                nc = c + dc
                if isAble(r, nc) and graph[r][nc] == "-": # 그 다음 타일도 연결된 경우
                    que.append([r,nc])
        if graph[r][c] == "|": # 위 아래 조사
            graph[r][c] = 0 # 방문 처리
            for dr in [-1, 1]:
                nr = r + dr
                if isAble(nr,c) and graph[nr][c]=="|":
                    que.append([nr, c])
    



answer = 0
for i in range(row):  
    for j in range(col):  
        if graph[i][j]!=0:  # 다음노드가 - 나 |일 경우 (아직 방문하지 않은 경우)
            bfs(i, j)  # 재귀함수 호출
            answer += 1

print(answer)


