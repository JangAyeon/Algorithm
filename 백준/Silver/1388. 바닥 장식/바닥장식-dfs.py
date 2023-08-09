import sys
input = sys.stdin.readline

row, col = map(int, input().split())
graph = [list(input().strip()) for _ in range(row)]
#print(row, col, graph)
answer=0


def isAble(r,c):
    if r<0 or c<0 or r>=row or c>=col:
        return False
    return True

def dfs(r, c):
    
    # 방문처리(0 값으로 교체)를 이곳 최상단에서 공통적으로 하는 경우 
    # 탐색해야하는 칸의 -(좌우), |(상하) 여부를 확인하는 조건문에 걸리지 않음
    
    # - 일떄
    if graph[r][c] == "-":
        graph[r][c] = 0 # 방문처리
        for dc in [1, -1]:  # 같은행: 양옆 확인
            nc = c + dc  
            if isAble(r, nc) and graph[r][nc]=="-": # 유효한 이동 영역 확인 -> - 좌우 탐색인지 확인
                dfs(r, nc)
    
    # | 일 때
    if graph[r][c]== "|":
        graph[r][c] = 0
        for dr in [-1, 1]:
            nr = r +  dr
            if isAble(nr,c) and graph[nr][c]=="|": # 유효한 이동 영역 확인 -> - 상하 탐색인지 확인
                dfs(nr,c)


answer = 0
for i in range(row):  
    for j in range(col):  
        if graph[i][j]=="|" or graph[i][j]=="-":  # 다음노드가 - 나 |일 경우 (아직 방문하지 않은 경우)
            dfs(i, j)  # 재귀함수 호출
            answer += 1

print(answer)


