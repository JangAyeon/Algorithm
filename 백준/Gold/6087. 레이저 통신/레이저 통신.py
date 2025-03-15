import sys
from collections import deque

# 표준 입력을 빠르게 받기 위해 sys.stdin.readline 사용
input = sys.stdin.readline

# 큰 수를 의미하는 무한대 값 (최소 거울 개수를 구하기 위해 사용)
INF = int(1e9)

# 방향 벡터 (서, 북, 동, 남)
dx = [0, -1, 0, 1]
dy = [-1, 0, 1, 0]

# 가로(W), 세로(H) 입력 받기
w, h = map(int, input().split())

# 'C' 위치 저장 배열
pos = []
# 지도 정보를 저장할 배열
board = []

# 지도 입력 받기
for i in range(h):
    board.append(list(input().strip()))  # 한 줄씩 리스트 형태로 저장
    for j in range(w):
        if board[i][j] == "C":  # 'C' 위치 찾기
            pos.append((i, j))

def bfs(sx, sy, ex, ey):
    """
    BFS를 이용해 시작점 (sx, sy)에서 끝점 (ex, ey)까지 최소 거울 개수를 찾는 함수
    """
    q = deque()  # BFS 탐색을 위한 큐
    # 방문 기록: 각 좌표 (x, y)에서 방향별 최소 거울 개수를 저장하는 3차원 배열
    visited = [[[INF] * 4 for _ in range(w)] for _ in range(h)]  # ✅

    # 시작 위치에서 네 방향으로 이동 시도
    for i in range(4):
        nx = sx + dx[i]
        ny = sy + dy[i]
        # 이동 가능하면 큐에 추가
        if 0 <= nx < h and 0 <= ny < w and board[nx][ny] != "*":
            q.append((nx, ny, i))  # (x, y, 방향)
            visited[nx][ny][i] = 0  # 처음 이동하는 곳이므로 거울 개수는 0

    # BFS 탐색 시작
    while q:
        x, y, direct = q.popleft()  # 큐에서 현재 위치와 방향을 꺼냄

        # 네 방향으로 이동 시도
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            # 이동 가능하고 벽이 아닐 경우
            if 0 <= nx < h and 0 <= ny < w and board[nx][ny] != "*":
                cnt = visited[x][y][direct]  # 현재 위치까지의 거울 개수

                # 방향이 바뀌면 거울을 추가해야 함
                if direct == 0 or direct == 2:  # 서쪽(0) 또는 동쪽(2)에서 이동
                    if i == 1 or i == 3:  # 북쪽(1) 또는 남쪽(3)으로 이동하면 거울 추가
                        cnt += 1
                else:  # 북쪽(1) 또는 남쪽(3)에서 이동
                    if i == 0 or i == 2:  # 서쪽(0) 또는 동쪽(2)으로 이동하면 거울 추가
                        cnt += 1

                # 방문한 적이 없는 경우
                if visited[nx][ny][i] == INF:
                    visited[nx][ny][i] = cnt
                    q.append((nx, ny, i))
                # 방문한 적이 있지만, 이전보다 더 적은 거울 개수로 이동 가능하면 갱신
                elif visited[nx][ny][i] > cnt:
                    visited[nx][ny][i] = cnt
                    q.append((nx, ny, i))

    # 도착점에서 네 방향 중 최소 거울 개수를 반환
    return min(visited[ex][ey])

# 시작점과 도착점 정보 전달하여 BFS 실행 후 결과 출력
print(bfs(pos[0][0], pos[0][1], pos[1][0], pos[1][1]))
