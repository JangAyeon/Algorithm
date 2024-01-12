def dfs(computers, visited, node):
    visited[node]=True
    for idx, value in enumerate(computers[node]):
        if idx!=node and value==1 and not(visited[idx]):
            dfs(computers, visited,idx)
            #print(node, idx, child)



def solution(n, computers):
    visited = [False] * n
    answer = 0
    start = 0
    visited[start] = start
    for node in range(n):
        if not(visited[node]):
            dfs(computers, visited, node)
            answer+=1

    return answer