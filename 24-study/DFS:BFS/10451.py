import sys
input = sys.stdin.readline
from collections import deque

def bfs(start):
    global answer
    que =deque()
    que.append(start)
    group=[start]
    while que:
        node = que.popleft()
        pair = arr[node]
        if not(visited[pair]):
            visited[pair]=True
            if pair in group:
                answer.append(group[group.index(pair):])
                break
            else:
                group.append(pair)
                que.append(pair)


T=int(input())

for _ in range(T):
    n = int(input())
    arr = [0]+list(map(int, input().split()))
    visited = [0 for _ in range(n+1)] 
    answer = []
    for idx in range(1, n+1):
        if not(visited[idx]):
            bfs(idx)
    print(len(answer))