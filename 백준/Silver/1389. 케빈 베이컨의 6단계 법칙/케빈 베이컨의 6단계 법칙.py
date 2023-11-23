from collections import deque
import sys
input = sys.stdin.readline

# 유저 수, 관계 수
n,m = map(int, input().split())

graph = [[] for _  in range(n+1)]

for _ in range(m):
    a,b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

answer=[]

def step(start):
    distance = [-1]*(n+1) # 초기화
    distance[start] = 0
    que = deque()
    que.append(start)
    while(que):
        curr = que.popleft()
        for next_ in graph[curr]:
            if (distance[next_]==-1):
                distance[next_]=distance[curr]+1
                que.append(next_)
            
    answer.append(sum(distance[1:]))
    

for i in range(1,n+1):
    step(i)

print(answer.index(min(answer))+1)