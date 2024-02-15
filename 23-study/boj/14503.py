import sys
input = sys.stdin.readline

n, m = map(int, input().split())
r, c, d = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]

# 0: 북, 1: 동, 2: 남, 3: 서
dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

# 방문: -1, 벽: 1, 빈칸: 0 
arr[r][c]=-1 
answer = 1

while arr[r][c]!=1:
    for _ in range(4):
        d = (d+3)%4
        nr, nc = r + dr[d], c + dc[d]
        flag = False # 4방향 다 탐색하고 빈칸 있는 지 여부 
        # 빈칸인 경우 
        if arr[nr][nc]==0:
            flag = True
            arr[nr][nc] = -1 # 방문 
            answer+=1
            r, c = nr, nc # 자리 이동 
            break
    if not(flag): # 빈칸 없었음 d-2를 통한 후진 
        r = r + dr[d-2]
        c = c + dc[d-2]

print(answer)
            
        


