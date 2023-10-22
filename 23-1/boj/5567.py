# 친구와 친구의 친구까지 초대
import sys
input = sys.stdin.readline
from collections import deque

# 동기 수 (1-indexing)
n = int(input())
# 리스트 길이
m = int(input())

graph = [[] for _ in range(n+1)]
visited = [False]*(n+1)

for _ in range(m):
    a,b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
    
def search(start):
    visited[start] = True
    que = deque()
    que.append([start,0])
    answer=0
    while que:
        node,connect = que.popleft()
        if connect==2:
            continue
        for nextNode in graph[node]:
            if not visited[nextNode]:
                answer+=1
                visited[nextNode]=True
                que.append([nextNode, connect+1])
    return answer
    
print(search(1))