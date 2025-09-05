def solution(k, dungeons):
    answer = -1
    
    n = len(dungeons)
    visited = [ False for _ in range(n)]
    
    
    def dfs(dept, lst, power):
        nonlocal answer
        answer = max(answer, len(lst))
        if(dept==n ):
            return
        for i in range(n):
            if(visited[i] or power<dungeons[i][0]):continue
            visited[i]=True
            dfs(dept+1, lst+ [i], power -dungeons[i][1] )
            visited[i]=False
    for start in range(n):
        visited[start]= True
        dfs(1, [start], k-dungeons[start][1])
        visited[start]=False
    
    return answer