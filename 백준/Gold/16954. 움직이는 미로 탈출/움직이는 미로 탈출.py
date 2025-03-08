from collections import deque

# 초기 맵 상태 입력
maps = [[list(input()) for _ in range(8)]]

# 벽이 한 칸씩 내려오는 8개의 맵 상태 생성
for i in range(8):
    temp_map = [list(row) for row in maps[i]]
    temp_map.insert(0, ['.'] * 8)  # 새로운 빈 줄 추가
    temp_map.pop()  # 마지막 줄 제거
    maps.append(temp_map)

# 초기 큐 설정 (시작 위치: (7,0), 경과 시간: 0)
queue = deque([(7, 0, 0)])
visited = [[0] * 8 for _ in range(8)]

# 이동 방향 (제자리, 8방향)
dx = [0, 1, -1, 0, 0, 1, 1, -1, -1]
dy = [0, 0, 0, 1, -1, 1, -1, 1, -1]

while queue:
    x, y, time = queue.popleft()

    # 목적지 도달했거나 시간이 8 이상이면 탈출 성공
    if (x == 0 and y == 7) or time >= 8:
        print(1)
        exit()

    for i in range(9):
        nx, ny = x + dx[i], y + dy[i]

        # 제자리에 머무를 경우 방문 처리 초기화
        if i == 0:
            visited[nx][ny] = 0

        # 이동 가능한 범위 내에 있고, 방문하지 않은 경우
        if 0 <= nx < 8 and 0 <= ny < 8 and visited[nx][ny] == 0:
            if maps[time][nx][ny] == '.':  # 현재 상태에서 이동 가능 여부 확인
                if maps[time + 1][nx][ny] != '#':  # 다음 상태에서 벽과 충돌하지 않는지 확인
                    queue.append((nx, ny, time + 1))
                    visited[nx][ny] = 1

print(0)
