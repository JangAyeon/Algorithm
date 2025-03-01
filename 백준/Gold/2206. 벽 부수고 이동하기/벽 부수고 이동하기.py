from collections import deque

def bfs(n, m, grid):
    # 상, 하, 좌, 우 방향 정의
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    # 방문 배열 (벽을 부쉈을 때와 아닐 때 두 개의 차원으로 관리)
    visited = [[[False] * 2 for _ in range(m)] for _ in range(n)]
    
    # BFS 큐 (x, y, 현재 거리, 벽 부숨 여부)
    queue = deque([(0, 0, 1, 0)])  # (row, col, distance, wall_broken)
    visited[0][0][0] = True  # 시작 위치 방문 처리 (벽 부수지 않음)

    while queue:
        x, y, dist, broken = queue.popleft()
        
        # 도착 지점에 도달하면 거리 반환
        if x == n - 1 and y == m - 1:
            return dist

        for dx, dy in directions:
            nx, ny = x + dx, y + dy

            # 맵을 벗어나지 않는지 확인
            if 0 <= nx < n and 0 <= ny < m:
                # 빈 칸이고, 아직 방문하지 않았다면
                if grid[nx][ny] == 0 and not visited[nx][ny][broken]:
                    visited[nx][ny][broken] = True
                    queue.append((nx, ny, dist + 1, broken))

                # 벽이고, 아직 벽을 부순 적이 없다면
                elif grid[nx][ny] == 1 and broken == 0 and not visited[nx][ny][1]:
                    visited[nx][ny][1] = True
                    queue.append((nx, ny, dist + 1, 1))  # 벽을 부순 상태로 추가

    return -1  # 도달할 수 없는 경우

# 입력 받기
n, m = map(int, input().split())
grid = [list(map(int, input().strip())) for _ in range(n)]

# 결과 출력
print(bfs(n, m, grid))
