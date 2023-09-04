import sys
input = sys.stdin.readline

# 보드 크기
n = int(input())
# 사과 갯수
k = int(input())

# 사과 위치 (1-index)
apple = [list(map(int, input().split())) for _ in range(k)]

# 방향 전환 횟수
l = int(input())
directions = {}
for _ in range(l):
    time, direction = input().split()
    directions[int(time)] = direction

# 아래, 오른쪽, 위, 왼쪽    
dr = [1,0, -1, 0]
dc = [0, +1, 0, -1]

def rotation(idx, cmd):
    if cmd=="D":
        idx = (idx-1)%4
    elif cmd =="L":
        idx = (idx+1)%4
    return idx
    
time = 0
snake = [[1,1]]
idx = 1

while True:
    time+=1
    r,c = snake[0]
    nr, nc = r +dr[idx], c + dc[idx]
    if not (1<=nr<=n and 1<=nc<=n):
        #print("벽",nr,nc)
        break
    if [nr, nc] in snake:
        #print("뱀")
        break
    snake.insert(0,[nr, nc])
    if [nr, nc] in apple:
        apple.remove([nr, nc])
    else:
        snake.pop()
    if time in directions.keys():
        idx = rotation(idx, directions[time])
    
print(time)