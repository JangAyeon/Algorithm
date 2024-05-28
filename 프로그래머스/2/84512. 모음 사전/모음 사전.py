

def solution(word):
    v = ["A","E","I","O","U"]
    n = len(v)
    visited = [[False for _ in range(n)] for _ in range(n)]
    answer = 0
    flag = False
    def dfs(words,dept):
        nonlocal answer
        nonlocal flag
        print(words, dept, answer)

        if "".join(words)==word:
            print(answer, dept)
            flag = True
            return
        if len(words)>n or dept>=n:
            return
        for i in range(n):
            if not(flag) and not visited[dept][i]:
                visited[dept][i]=True
                answer+=1
                dfs(words+[v[i]], dept+1)
                visited[dept][i]=False
    dfs([],0)
    return answer
