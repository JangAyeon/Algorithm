from collections import deque

# 입력 받기
n, m = map(int, input().split())  # n: 열(M), m: 행(N)
castle = [list(map(int, input().split())) for _ in range(m)]

# 방향 벡터 (서, 북, 동, 남) - 벽 비트값 (1, 2, 4, 8)
dx = [0, -1, 0, 1]
dy = [-1, 0, 1, 0]

# 방문 배열 및 방 크기 저장
visited = [[False] * n for _ in range(m)]
room_sizes = []

def bfs(sx, sy):
    queue = deque([(sx, sy)])
    visited[sx][sy] = True
    room_size = 0
    
    while queue:
        x, y = queue.popleft()
        room_size += 1
        
        for i in range(4):  # 4방향 탐색
            if not (castle[x][y] & (1 << i)):  # 해당 방향에 벽이 없으면 이동 가능
                nx, ny = x + dx[i], y + dy[i]
                if 0 <= nx < m and 0 <= ny < n and not visited[nx][ny]:
                    visited[nx][ny] = True
                    queue.append((nx, ny))
                    
    return room_size

# 1. 방 개수 및 최대 방 크기 찾기
room_count = 0
max_room_size = 0

for i in range(m):
    for j in range(n):
        if not visited[i][j]:  # 방문하지 않은 곳이면 BFS 실행
            room_size = bfs(i, j)
            room_sizes.append(room_size)
            max_room_size = max(max_room_size, room_size)
            room_count += 1

# 2. 벽을 하나 제거하고 얻을 수 있는 가장 큰 방 크기 찾기
max_combined_size = 0

for i in range(m):
    for j in range(n):
        for k in range(4):  # 4방향의 벽을 제거하는 경우 고려
            ni, nj = i + dx[k], j + dy[k]
            if 0 <= ni < m and 0 <= nj < n and (castle[i][j] & (1 << k)):  # 벽이 있는 경우만
                visited = [[False] * n for _ in range(m)]
                castle[i][j] -= (1 << k)  # 벽 제거
                new_size = bfs(i, j)
                max_combined_size = max(max_combined_size, new_size)
                castle[i][j] += (1 << k)  # 벽 복구

# 출력
print(room_count)
print(max_room_size)
print(max_combined_size)
