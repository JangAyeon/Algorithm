def solution(begin, target, words):
    answer = []
    N = len(words)
    visited = [ False for _ in range(N)]
    def countDiff(str1, str2):
        count = 0
        for s1, s2 in zip(str1, str2):
            if(s1!=s2):count+=1
        return count
    
    def dfs(start, dept, lst):
        if(start==target):
            answer.append(dept)
            return
        for idx, v in enumerate(words):
            if(visited[idx] or countDiff(v, start)>1):
                continue
            visited[idx]=True
            dfs(v, dept+1, lst+[v])
            visited[idx]=False
    dfs(begin, 0, [begin])
    return min(answer) if len(answer)>0 else 0