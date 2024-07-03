import sys
input = sys.stdin.readline
from collections import deque

T = int(input())
##  자기 위치와 뒤쳐진 인물의 수가 일치하지 않는다면 불가능한 경우

def topologySort(graph, indegree, que):
    answer = []
    while que:
        node = que.popleft()
        ##print(node, indegree[node], graph[node])
        
        answer.append(node)
        for next_ in graph[node]:
            ##print(next_, indegree[next_])
            indegree[next_]-=1
            if indegree[next_]==0:
                que.append(next_)

    if sum(indegree)>0:
        return ["IMPOSSIBLE"]
    else:
        return answer

for _ in range(T):
    n = int(input())
    arr = list(map(int, input().split()))
    graph = [[] for _ in range(n+1)]
    indegree = [0 for _ in range(n+1)]

    flag=False
    que = deque()
    q = int(input())

    for i in range(n):
        graph[arr[i]] = arr[i+1:]
        indegree[arr[i]]+=i

    ##print(graph, indegree)

    for _ in range(q):
        a,b = map(int, input().split())
        if a in graph[b]:
            indegree[b]+=1
            indegree[a]-=1
            graph[b].remove(a)
            graph[a].append(b)
        else:
            indegree[a]+=1
            indegree[b]-=1
            graph[a].remove(b)
            graph[b].append(a)

    ##print(indegree, graph)

    for idx in range(1,n+1):
        if indegree[idx]==0:
            que.append(idx)
    ##print(que)
    if len(que)!=1:
        flag = True


    if flag:
        print("IMPOSSIBLE")
    else:
        print(*topologySort(graph, indegree, que))




