

def solution(tickets):
    answer = []
    visited = [False]*(len(tickets))
    answer = []
    def dfs(dept, city,route):
        if dept>=len(tickets):
            answer.append(route)
            return
        for idx, (curr_, next_) in enumerate(tickets):
            if city==curr_ and not(visited[idx]):
                visited[idx]=True
                
                dfs(dept+1,next_,route+[next_])
                visited[idx]=False

    dfs(0, "ICN",["ICN"])      
    answer.sort()
    return answer[0]