import sys
input = sys.stdin.readline
INF=int(1e9)

# 도시 갯수, 버스 갯수
n = int(input())
m = int(input())
# 시작도시, 도착도시, 비용 (버스 정보)
arr = [list(map(int, input().split())) for _ in range(m)]
graph = [[INF]*(n+1) for _ in range(n+1)]



for start, end, cost in arr:
    graph[start][end] = min(graph[start][end], cost)

for i in range(1, n+1):
        graph[i][i] = 0
    
for mid in range(1,n+1):
    for start in range(1,n+1):
        for end in range(1,n+1):
            curr_cost  = graph[start][mid]+graph[mid][end]
            graph[start][end] = min(graph[start][end],curr_cost)
                

for row in range(1, n+1):
    for col in range(1, n+1):
        if graph[row][col] ==INF: # 무한대인 경우
            print(0, end = " ")
        else:
            print(graph[row][col], end = " ")
    print()