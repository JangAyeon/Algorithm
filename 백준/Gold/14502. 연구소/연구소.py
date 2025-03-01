from itertools import combinations
from collections import deque
import copy

# 입력 받기
N, M = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]

# 빈 칸과 바이러스 위치 저장
empty_spaces = []
virus_positions = []

for i in range(N):
    for j in range(M):
        if graph[i][j] == 0:
            empty_spaces.append((i, j))
        elif graph[i][j] == 2:
            virus_positions.append((i, j))

# 4방향 이동 정의
directions = [
    [-1,0],[1,0],
    [0,-1],[0,1]
]

## 바이러스를 퍼뜨리고 남은 안전 영역 크기를 반환
def spread_virus(graph):
    queue = deque(virus_positions)
    temp_map = copy.deepcopy(graph)  # 원본 배열 보존

    while queue:
        r, c = queue.popleft()
        for [dr, dc] in directions:
            nr, nc = r + dr, c + dc
            ## 범위 밖 || 빈칸(0) 
            if(not(0 <= nr < N) or not( 0 <= nc < M ) or temp_map[nr][nc]!=0):
                continue
            temp_map[nr][nc] = 2
            queue.append((nr, nc))

    return sum(row.count(0) for row in temp_map)  # 남은 안전 영역 크기 반환

# 벽을 세울 수 있는 모든 조합 시도
max_safe_area = 0
for walls in combinations(empty_spaces, 3):
    # 벽 세우기
    for x, y in walls:
        graph[x][y] = 1

    # 바이러스 퍼트리고 안전 영역 계산
    max_safe_area = max(max_safe_area, spread_virus(graph))

    # 벽 복구
    for x, y in walls:
        graph[x][y] = 0

# 결과 출력
print(max_safe_area)
