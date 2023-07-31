import collections

n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
def bfs():
    queue = collections.deque()
    queue.append((0,0))
    check = [[False] * m for _ in range(n)]
    dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
    count = 0
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                if graph[nx][ny] == 0 and check[nx][ny] == False:
                    check[nx][ny] = True
                    queue.append((nx,ny))
                # (0,0) 에서 시작해서 처음 만나는 1들은 모두 가장자리이다.
                elif graph[nx][ny] == 1:
                    # queue에 추가해주는게 아니라 0으로 바꿔줘 녹게만들어준다.
                    graph[nx][ny] = 0
                    count += 1
                    check[nx][ny] = True
    return count

result = []
time = 0
while True:
    count = bfs()
    result.append(count)
    # count가 0이면 모든 치즈가 녹았다는 소리이다.
    if count == 0:
        break
    time += 1

print(time)
# 한시간 전에(모두 녹기전 단계) count를 출력해야 되므로 [-2]를 출력한다.
print(result[-2])