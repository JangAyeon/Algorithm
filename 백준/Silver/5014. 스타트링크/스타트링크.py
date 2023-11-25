from collections import deque
F, S, G, U, D = map(int, input().split())
que= deque()
que.append([S,0])
visited = [False]*(F+1)
flag = False
while que:
    currNode, currDist = que.popleft()
    if currNode==G:
        print(currDist)
        flag = True
        break
    for step in [+U, -D]:
        temp = step+currNode
        if 0<temp<=F and not(visited[temp]):
            que.append([temp, currDist+1])
            visited[temp]=True

if not(flag):
    print("use the stairs")