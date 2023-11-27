from collections import deque

# 가수 수 N, 보조 PD 수 M
N,M = map(int, input().split())
arr = [list(map(int, input().split()[1:])) for _ in range(M)]
indegree = [0 for _ in range(N+1)]
graph = [[] for _ in range(N+1)]

answer = []

for pd in arr:
    for idx in range(len(pd)-1):
        a, b = pd[idx], pd[idx+1]
        graph[a].append(b)
        indegree[b]+=1

que = deque()

for i in range(1, N+1):
    if indegree[i]==0:
        que.append(i)


while que:
    curr = que.popleft()
    answer.append(curr)
    for next_ in graph[curr]:
        indegree[next_]-=1
        if indegree[next_]==0:
            que.append(next_)

if len(answer)!=N:
    print(0)
else:
    for i in answer:
        print(i)