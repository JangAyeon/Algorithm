def solution(info, edges):
    visited = [False]*len(info)
    wolf = sheep = 0
    answer = []
    
    # 0 : 양, 1 : 늑대
    
    def dfs(sheep, wolf):
        if sheep>wolf:
            answer.append(sheep)
        else:
            return
        
        for p, c in edges:
            if visited[p] and not(visited[c]):
                visited[c] = True
                if info[c] == 0:
                    dfs(sheep+1, wolf)
                else:
                    dfs(sheep, wolf+1)
                visited[c] = False
    
    # 루트 노드 (양) 방문
    visited[0] = True
    dfs(sheep+1, wolf)
    answer = max(answer)

    return answer