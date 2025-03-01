from itertools import combinations
from collections import deque
import copy

# 입력 받기
N, M = map(int, input().split())
lab = [list(map(int, input().split())) for _ in range(N)]

# 빈 칸과 바이러스 위치 저장
empty_spaces = []
virus_positions = []

for i in range(N):
    for j in range(M):
        if lab[i][j] == 0:
            empty_spaces.append((i, j))
        elif lab[i][j] == 2:
            virus_positions.append((i, j))

# 4방향 이동 정의
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def spread_virus(lab_map):
    """ 바이러스를 퍼뜨리고 남은 안전 영역 크기를 반환 """
    queue = deque(virus_positions)
    temp_map = copy.deepcopy(lab_map)  # 원본 배열 보존

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < N and 0 <= ny < M and temp_map[nx][ny] == 0:
                temp_map[nx][ny] = 2
                queue.append((nx, ny))

    return sum(row.count(0) for row in temp_map)  # 남은 안전 영역 크기 반환

# 벽을 세울 수 있는 모든 조합 시도
max_safe_area = 0
for walls in combinations(empty_spaces, 3):
    # 벽 세우기
    for x, y in walls:
        lab[x][y] = 1

    # 바이러스 퍼트리고 안전 영역 계산
    max_safe_area = max(max_safe_area, spread_virus(lab))

    # 벽 복구
    for x, y in walls:
        lab[x][y] = 0

# 결과 출력
print(max_safe_area)
