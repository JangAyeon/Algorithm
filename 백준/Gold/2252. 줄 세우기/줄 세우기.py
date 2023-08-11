from collections import deque
import sys
input = sys.stdin.readline

# 학생 1번 ~ N번, 키 비교 횟수
n,m = map(int, input().split())
indegree = [0]*(n+1)
graph = [[] for _ in range(n+1)]

for _ in range(m):
    start, end = map(int, input().split())
    graph[start].append(end)
    indegree[end]+=1
    

def topology_sort():
    que = deque()
    result = []
    
    for i in range(1, n+1):
        if indegree[i]==0:
            que.append(i)
    while que:
        now = que.popleft()
        result.append(now)
        
        for i in graph[now]:
            indegree[i]-=1
            if indegree[i]==0:
                que.append(i)
              
    print(*result)
    
topology_sort()