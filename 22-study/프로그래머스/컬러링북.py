from collections import deque 
import sys
input = sys.stdin.readline


def solution(m,n,picture):
    area = 0
    max_size = 0
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]

    que = deque()
    for i in range(m):
        for j in range(n):
            if not picture[i][j]: # 이미 방문한 경우
                continue
            else:
                area+=1
                count=0
                que.append([i,j])
                color = picture[i][j]
                picture[i][j] = 0 # 방문 표시

                while que:
                    count+=1
                    x, y = que.popleft()
                    for k in range(4):
                        nx, ny  = x + dx[k], y + dy[k]
                        if 0<= nx < m and 0<= ny < n and picture[nx][ny]==color: # 그림 영역 내 좌표 & 같은 색깔 영역
                            que.append([nx, ny])
                            picture[nx][ny] = 0 # 방문 표시

            max_size = max(max_size, count)

    return [area, max_size]



testcase = [[6,4, [[1, 1, 1, 0], [1, 2, 2, 0], [1, 0, 0, 1], [0, 0, 0, 1], [0, 0, 0, 3], [0, 0, 0, 3]]],[6,4, [[1, 1, 1, 0], [1, 1, 1, 0], [0, 0, 0, 1], [0, 0, 0, 1], [0, 0, 0, 1], [0, 0, 0, 1]]]]

for m,n,picture in testcase:
    print(solution(m,n,picture)) #[4,5], [2, 6] 