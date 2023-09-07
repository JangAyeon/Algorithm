import sys
input = sys.stdin.readline
from collections import deque
# 컴퓨터 수 (1-indexing)
n = int(input())
# 간선 수
m = int(input())
graph = [[] for _ in range(n+1)]
visited = [0]*(n+1)

for _ in range(m):
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

def spread(start):
    que = deque()
    que.append(start)
    visited[start]=1
    while que:
        node = que.popleft()
        for nextNode in graph[node]:
            if not visited[nextNode]:
                que.append(nextNode)
                visited[nextNode]=1
            
            
spread(1)
print(sum(visited[2:]))


"""
1
0
ans: 0
"""

"""
3
2
1 3
2 3
ans: 2
"""