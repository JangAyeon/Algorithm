from collections import deque
import sys

input = sys.stdin.read
sys.setrecursionlimit(10**6)

# 방향 (상, 하, 좌, 우)
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(start_x, start_y, w, h, room):
    """ BFS를 이용해 start_x, start_y에서 모든 더러운 칸까지의 최단 거리 계산 """
    queue = deque([(start_x, start_y, 0)])
    distances = [[-1] * w for _ in range(h)]
    distances[start_x][start_y] = 0

    while queue:
        x, y, dist = queue.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < h and 0 <= ny < w and room[nx][ny] != 'x' and distances[nx][ny] == -1:
                distances[nx][ny] = dist + 1
                queue.append((nx, ny, dist + 1))
    
    return distances

def solve_case(w, h, room):
    """ 한 개의 테스트 케이스를 해결 """
    # 로봇과 더러운 칸 위치 찾기
    dirty_positions = []
    robot_x = robot_y = -1

    for i in range(h):
        for j in range(w):
            if room[i][j] == 'o':  # 로봇 시작 위치
                robot_x, robot_y = i, j
            elif room[i][j] == '*':  # 더러운 칸 위치
                dirty_positions.append((i, j))

    # 로봇 + 더러운 칸 좌표들
    all_positions = [(robot_x, robot_y)] + dirty_positions
    num_dirty = len(dirty_positions)

    # 각 지점 간 최단 거리 구하기
    dist_matrix = [[-1] * (num_dirty + 1) for _ in range(num_dirty + 1)]
    for i, (x, y) in enumerate(all_positions):
        distances = bfs(x, y, w, h, room)
        for j, (dx, dy) in enumerate(all_positions):
            dist_matrix[i][j] = distances[dx][dy]

    # 연결 불가능한 경우 확인
    for i in range(num_dirty + 1):
        for j in range(num_dirty + 1):
            if i != j and dist_matrix[i][j] == -1:
                return -1

    # TSP (비트마스킹 DP)로 최소 이동 횟수 계산
    INF = float('inf')
    dp = [[INF] * (1 << (num_dirty + 1)) for _ in range(num_dirty + 1)]
    dp[0][1] = 0  # 로봇 위치에서 시작

    for mask in range(1 << (num_dirty + 1)):  # 모든 상태를 순회
        for i in range(num_dirty + 1):  # 현재 위치
            if not (mask & (1 << i)):  # i번째 지점이 방문되지 않음
                continue
            for j in range(num_dirty + 1):  # 다음 위치
                if mask & (1 << j):  # 이미 방문한 곳은 패스
                    continue
                next_mask = mask | (1 << j)
                dp[j][next_mask] = min(dp[j][next_mask], dp[i][mask] + dist_matrix[i][j])

    # 모든 더러운 칸을 방문한 상태에서 최소 이동 횟수 반환
    return min(dp[i][(1 << (num_dirty + 1)) - 1] for i in range(num_dirty + 1))


    """ 여러 개의 테스트 케이스 처리 """
data = input().splitlines()
index = 0

while index < len(data):
    w, h = map(int, data[index].split())
    if w == 0 and h == 0:
        break
    room = [list(data[index + i + 1]) for i in range(h)]
    index += h + 1

    print(solve_case(w, h, room))


