from collections import deque

def solution(m,n,picture):
    dx = [-1,1,0,0]
    dy = [0,0,-1,1]
    que = deque()
    max_size = 0
    area = 0
    for i in range(m):
        for j in range(n):
            if not picture[i][j]: # 방문한 곳
                continue
            else:
                area +=1
                count = 0
                color = picture[i][j]
                picture[i][j] = 0
                que.append([i,j])

                while que:
                    count+=1
                    x, y =  que.popleft()
                    for k in range(4):
                        nx, ny = x + dx[k], y + dy[k]
                        if 0<= nx <m and 0<= ny < n and picture[nx][ny]==color:
                            picture[nx][ny]=0
                            que.append([nx, ny])
                max_size =max(count, max_size)
    return [area, max_size]





testcase = [[6,4, [[1, 1, 1, 0], [1, 2, 2, 0], [1, 0, 0, 1], [0, 0, 0, 1], [0, 0, 0, 3], [0, 0, 0, 3]]],[6,4, [[1, 1, 1, 0], [1, 1, 1, 0], [0, 0, 0, 1], [0, 0, 0, 1], [0, 0, 0, 1], [0, 0, 0, 1]]]]
for m,n,picture in testcase:
    print(solution(m,n,picture)) #[4,5], [2, 6] 