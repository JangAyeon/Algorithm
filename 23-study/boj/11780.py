import sys
input = sys.stdin.readline
INF=int(1e9)

# 도시 갯수, 버스 갯수
n = int(input())
m = int(input())
# 시작도시, 도착도시, 비용 (버스 정보)
arr = [list(map(int, input().split())) for _ in range(m)]
nxt = [[0]*(n+1) for _ in range(n+1)]
graph = [[INF]*(n+1) for _ in range(n+1)]



for start, end, cost in arr:
    if graph[start][end]>cost:
        graph[start][end] = cost
        nxt[start][end] = end

for i in range(1, n+1):
        graph[i][i] = 0
    
for mid in range(1,n+1):
    for start in range(1,n+1):
        for end in range(1,n+1):
            curr_cost  = graph[start][mid]+graph[mid][end]
            if graph[start][end]>curr_cost:
                graph[start][end] = curr_cost
                nxt[start][end] = nxt[start][mid]
                

for row in range(1, n+1):
    for col in range(1, n+1):
        if graph[row][col] ==INF: # 무한대인 경우
            print(0, end = " ")
        else:
            print(graph[row][col], end = " ")
    print()
    
for start in range(1, n+1):
    for end in range(1, n+1):
        #print("start",start, "end", end, ": ",graph[start][end])
        if graph[start][end]==INF or graph[start][end]==0:
            print(0)
        else:
            temp = []
            pos = start
            while True:
                temp.append(pos)
                if pos==end:
                    break
                pos = nxt[pos][end]
            print(len(temp),*temp)
                
"""
input:
4
4
1 2 1
1 3 1
3 2 1
2 1 1
    
correct answer:
0 1 1 0 
1 0 2 0 
2 1 0 0 
0 0 0 0 
0
2 1 2
2 1 3
0
2 2 1
0
3 2 1 3
0
3 3 2 1
2 3 2
0
0
0
0
0
0

"""
