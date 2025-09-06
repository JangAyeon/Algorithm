def solution(tickets):
    answer = []
    N = len(tickets)
    visited = [False for _ in range(N)]
    def dfs(curr, route, dept):
        ## print(route, dept)
        if(dept==N):
            answer.append(" ".join(route))
            
        for idx,next_ in enumerate(tickets):
            [start, end]=next_
            
            if(curr!=start or visited[idx]):
                continue
            
            visited[idx]=True
            dfs(end, route+[end], dept+1)
            visited[idx]=False
    dfs("ICN",["ICN"],0)
    answer.sort()
    ### print(answer)
    return answer[0].split(" ")