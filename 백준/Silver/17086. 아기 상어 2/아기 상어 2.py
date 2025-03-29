import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().strip().split())

grid = [list(map(int, input().split())) for _ in range(n)]

# 인접 방향(대각선 포함)
directions = [(-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1)]

def bfs(row, col):
    q = deque()
    q.append((row, col))
    visited = [[0] * m for _ in range(n)]
    found_shark = False  # flag
    
    while q:
        row, col = q.popleft()
        
        for dr, dc in directions:
            new_row, new_col = row + dr, col + dc
            
            if 0 <= new_col < m and 0 <= new_row < n and visited[new_row][new_col] == 0:
                if grid[new_row][new_col] == 0:
                    q.append((new_row, new_col))
                    visited[new_row][new_col] = visited[row][col] + 1
                else:
                    max_distance = visited[row][col] + 1
                    found_shark = True
        
        if found_shark:
            break
    
    return max_distance

max_distance = 0
for row in range(n):
    for col in range(m):
        if grid[row][col] != 1:
            max_distance = max(max_distance, bfs(row, col))

print(max_distance)