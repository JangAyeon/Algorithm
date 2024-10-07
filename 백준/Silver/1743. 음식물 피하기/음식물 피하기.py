from collections import deque

n, m, k = map(int, input().split())
arr = [[0]*m for _ in range(n)]

for _ in range(k):
    a, b = map(int, input().split())
    arr[a-1][b-1] = 1

direct = [(1, 0), (-1, 0), (0, 1), (0, -1)]
visit = [[0]*m for _ in range(n)]
ans = 0

def bfs(r,c):

    que = deque([(r, c)])
    cnt = 1
    visit[r][c] = 1

    while que:
        r, c = que.popleft()
        
        for d in direct:
            nr, nc = r+d[0], c+d[1]
            if not(0 <= nr < n) or not(0 <= nc < m) or visit[nr][nc] or not(arr[nr][nc]):
                continue
            visit[nr][nc] = 1
            que.append((nr, nc))
            cnt += 1
    return cnt

for r in range(n):
    for c in range(m):
        if arr[r][c] and not visit[r][c]:

            ans = max(ans, bfs(r,c))

print(ans)