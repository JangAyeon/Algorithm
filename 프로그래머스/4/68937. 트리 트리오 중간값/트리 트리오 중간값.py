from collections import deque

def BFS(tree, start):
    distance = []
    q = deque()
    q.append([start, 0]) # 시작 위치와 거리!
    visit = {start : True} # 시작 위치를 방문했었으면 True라고 입력해준다.

    while q:
        curr, dist = q.popleft()
        distance.append([curr, dist])

        for node in tree[curr]:
            if node not in visit:
                q.append([node, dist+1])
                visit[node] = True

    return distance

def solution(n, edges):
    tree = [[] for _ in range(n+1)]
    for a,b in edges:
        tree[a].append(b)
        tree[b].append(a)

    # 루트에서 가장 멀리 떨어진 노드 탐색    
    leaf = BFS(tree, 1)
    # 루트에서 가장 멀리 떨어진 노드에서 거리 탐색
    farther = BFS(tree, leaf[-1][0])

    # 거리가 가장 먼 leaf가 두개 이상일 경우
    if leaf[-1][1] == leaf[-2][1]:
        return farther[-1][1]
    else:
        # 해당 리프에서 두번째로 멀리 떨어진 길이가 중간값. 
        return farther[-2][1]