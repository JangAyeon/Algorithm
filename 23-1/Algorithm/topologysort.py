from collections import deque

v,e = map(int, input().split())
indegree = [0]*(v+1)
graph = [[] for _ in range(v+1)]

# 방향 그래프의 간선 정보 입력 받기
for _ in range(e):
    start, end = map(int, input().split())
    graph[start].append(end)
    indegree[end]+=1 # 진입 차수 1 증가
    
    
    
def topology_sort():
    result = []
    que = deque()
    # 처음 시작할 때 진입 차수가 0인 노드를 큐에 삽입
    for i in range(1,v+1):
        if indegree[i]==0:
            que.append(i)
    # 큐가 빌 때까지 반복
    while que:
        now = que.popleft()
        result.append(now)
        # 해당 노드와 연결된 노드들의 진입차수에서 1 빼기
        for i in graph[now]:
            indegree[i]-=1
            if indegree[i]==0:
                que.append(i)
    # 위상 정렬 결과 출력
    print(*result)
    
topology_sort()

"""
1 2
1 5
2 3
2 6
3 4
4 7
5 6
6 4

1 2 5 3 6 4 7
"""