import sys
input = sys.stdin.readline
from collections import deque

n, m = map(int, input().split())
graph = [list(input().strip()) for _ in range(n)]
cnt = int(input())
cmd = list(map(int, input().split()))

def destroy(row, turn):
    if turn%2==1: ## 오른쪽
        start = m-1
        end = -1
        gap =-1
    else: ## 왼쪽
        start = 0
        end = m
        gap=+1
    for col in range(start, end, gap):
        if graph[row][col]=="x":
            graph[row][col]="."
            break
    return graph

def find_cluster(graph):
    visit = [[False for _ in range(m)] for _ in range(n)]
    dir = [[-1, 0],[1,0],[0,-1],[0,+1]]
    que = deque()
    ## 바닥에서부터 연결된 미네랄 덩이 탐색 (클러스터 탐색) 
    for i in range(m):
        if graph[n-1][i] == 'x':
            que.append((n-1, i))
    while que:
        r, c = que.popleft()
        for dr, dc in dir:
            nr,nc = r+dr,c+dc
            if not(0<=nr<n) or not(0<=nc<m) or visit[nr][nc]:
                continue

            if graph[nr][nc] == 'x':
                visit[nr][nc] = True
                que.append((nr, nc))

    ## 미네랄인데 바닥에서부터 탐색과정에서 방문되지 않은 미네랄이면 공중에 떠있는 미네랄임
    ## => 움직이기 처리가 필요한 미네랄
    cluster = []
    for r in range(n-1, -1, -1):
        for c in range(m):
            if graph[r][c] == 'x' and not(visit[r][c]):
                # 클러스터 발생
                cluster.append([r,c])
    if len(cluster) > 0:
        return cluster, 1, visit  # cluster 있음
    else:
        return cluster, 0, visit  # cluster 없음
    
def move_cluster(graph, cluster, visited):
    min_dr = float("inf")

    for r,c in cluster:
        down = 0
        for nr in range(r+1, n):
            if graph[nr][c]==".":
                down+=1
            elif graph[nr][c]=="x" and visited[nr][c]:
                break
        min_dr = min(min_dr, down)
    
    for r, c in cluster:
        graph[r][c]="."
        graph[r+min_dr][c]="x"
    return graph

for i in range(cnt): # 막대를 던지는 횟수만큼 반복
    # 1) 미네랄 파괴
    graph = destroy(n - cmd[i], i) # 바닥부터 1
    # 2) 클러스터 조사
    cluster, check, visited = find_cluster(graph)
    # 3) 클러스터 이동
    if check == 1:
        graph = move_cluster(graph, cluster, visited)




for i in range(n):
    print("".join(graph[i]))