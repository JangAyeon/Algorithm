import sys
input = sys.stdin.readline
from collections import deque


def bfs(i):
    que = deque([i])
    groups[i] = 1
    while que:
        curr = que.popleft()
        color = groups[curr]%2+1
        for next_ in graph[curr]:
            if not(groups[next_]): ## 이전에 그룹 배정받은 적 없는 경우
                groups[next_] = color
                que.append(next_)
                ## 이전에 배정 받은 그룹과 지금 그룹이 다른 경우
            elif groups[next_]!=color:
                return False
        
    
    return True

T = int(input())

for _ in range(T):
    answer = "YES"
    v,e = map(int, input().split())
    groups = [0 for _ in range(v+1)] # 이분 그래프 그룹 1과 2
    graph = [[] for _ in range(v+1)]
    
    for _ in range(e):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)

    for i in range(1, v+1):
        if not(groups[i]):
            if not(bfs(i)):
                answer = "NO"
                break

    print(answer)



