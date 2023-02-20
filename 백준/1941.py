from collections import deque
import sys
input = sys.stdin.readline

arr = [list(input()) for _ in range(5)]
cnt = 0
dy = [1,-1,0,0]
dx = [0,0,1,-1]

def check_s(cur):
    s_cnt = 0
    for x, y in cur:
        if arr[x][y] == 'S':
            s_cnt += 1
    return False if s_cnt < 4 else True

def check_adjacent(cur):
    visited = [False] * 7
    q = deque()
    q.append(cur[0])
    visited[0] = True

    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if (nx, ny) in cur:
                idx = cur.index((nx, ny))
                if not visited[idx]:
                    q.append((nx, ny))
                    visited[idx] = True

    return False if False in visited else True

def func(k, idx, cur):
    global cnt
    if k == 7:
        if check_s(cur) and check_adjacent(cur):
            cnt += 1
        return
    for i in range(idx, 25):
        func(k + 1, i + 1, cur + [divmod(i, 5)])

func(0, 0, [])
print(cnt)