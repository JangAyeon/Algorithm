

def solution(word):
    v = ["A","E","I","O","U"]
    n = len(v)
    visited = [[False for _ in range(n)] for _ in range(n)]
    answer = 0
    flag = False
    def dfs(words,dept):
        nonlocal answer
        nonlocal flag
        
        if "".join(words)==word:
            print(answer)
            flag = True
            return 
        for i in range(n):
            if dept>=5 or flag:
                return
            if not visited[dept][i]:
                answer+=1
                visited[dept][i]=True
                dfs(words+[v[i]], dept+1)
                visited[dept][i]=False
    dfs([],0)
    return answer
