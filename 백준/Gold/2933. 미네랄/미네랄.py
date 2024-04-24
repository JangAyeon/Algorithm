import sys
input = sys.stdin.readline
from collections import deque

# 왼, 오 순서대로 미네랄을 파괴
    # 미네랄을 파괴하면 그 즉시 탐색 stop
# 파괴 후 클러스터 발생 시(공중에 떠있으면 안됨)
    # - 바닥과 만날 때까지 이동
    # - 또 다른 미네랄을 만날 때 까지 이동

R, C = map(int, input().split())
graph = []
for i in range(R):
    graph.append(list(input().strip()))

cnt = int(input()) # 막대 던지는 횟수
hlist = list(map(int,input().split()))



def destroy_mi(y, turn): # 미네랄 파괴
    if turn%2==1:
        start = C-1
        end = -1
        gap = -1
    else:
        start = 0
        end = C
        gap = +1

    for i in range(start, end, gap):
        if graph[y][i]=="x":
            graph[y][i]="."
            break
    
    return graph


def find_cluster(graph):
    visit = [[False for _ in range(C)] for _ in range(R)]
    dir = [[-1, 0],[1,0],[0,-1],[0,+1]]
    que = deque()
    for i in range(C):
        if graph[R-1][i] == 'x':
            que.append((R-1, i))
    while que:
        r, c = que.popleft()
        for dr, dc in dir:
            nr,nc = r+dr,c+dc
            if not(0<=nr<R) or not(0<=nc<C) or visit[nr][nc]:
                continue

            if graph[nr][nc] == 'x':
                visit[nr][nc] = True
                que.append((nr, nc))

    cluster = []
    for r in range(R-1, -1, -1):
        for c in range(C):
            if graph[r][c] == 'x' and not(visit[r][c]):
                # 클러스터 발생
                cluster.append([r,c])
    if len(cluster) > 0:
        return cluster, 1, visit  # cluster 있음
    else:
        return cluster, 0, visit  # cluster 없음

def move_cluster(graph, cluster, visit):
    down_min = 1e9
    for r, c in cluster:
        down_cnt = 0
        for nr in range(r+1, R):
            if graph[nr][c] == '.':
                down_cnt += 1
            elif graph[nr][c] == 'x' and visit[nr][c]:
                break
        down_min = min(down_min, down_cnt)
    for r, c in cluster:
        graph[r][c] = '.'
        graph[r+down_min][c] = 'x'
    return graph

for i in range(cnt): # 막대를 던지는 횟수만큼 반복
    # 1) 미네랄 파괴
    graph = destroy_mi(R - hlist[i], i) # 바닥부터 1
    # 2) 클러스터 조사
    cluster, check, visit = find_cluster(graph)
    # 3) 클러스터 이동
    if check == 1:
        graph = move_cluster(graph, cluster, visit)


for i in range(R):
    print("".join(graph[i]))
