import sys
sys.setrecursionlimit(10 ** 8)

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

def dfs(n, m, row, col, board): #치즈 외부 공간과 내부 공간을 구분하는 dfs 함수
    if row < 0 or row >= n or col < 0 or col >= m or board[row][col] != 0:
        return
    board[row][col] = -1 #외부 공기로 표시
    for i in range(4):
        dfs(n, m, row + dr[i], col + dc[i], board)

def canMelt(row, col, board):
    cnt = 0
    for i in range(4):
        nr = row + dr[i]
        nc = col + dc[i]
        if board[nr][nc] == -1:
            cnt += 1 #외부 공간
    return cnt >= 2

def findCheese(n, m, board): 
    cheese = list()
    for i in range(n):
        for j in range(m):
            #녹지 않은 치즈면서, 이번에 녹일 수 있다면
            if board[i][j] == 1 and canMelt(i, j, board): 
                cheese.append([i, j])
    return cheese

def solution(n, m, board):
    # 전역으로 선언된 배열에 주어진 배열 복사
    answer = 0 #시간
    dfs(n, m, 0, 0, board) #외부 공간 표시
    while True:
        cheese = findCheese(n, m, board) #이번에 녹을 치즈들
        if not cheese: #더 이상 녹을 치즈가 없다면 종료
            break           
        #치즈를 녹이고, 새롭게 생긴 외부 공간 표시
        for a in cheese:
            row, col = a
            board[row][col] = 0
            dfs(n, m, row, col, board)
        answer += 1
    return answer

if __name__ == "__main__":
    #입력
    input = sys.stdin.readline
    n, m = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(n)]
    #연산
    answer = solution(n, m, board);    
    #출력
    print(answer)