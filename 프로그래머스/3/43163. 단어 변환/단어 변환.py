## 한개만 다른지 판별하는 함수
def diff(w,t):
    count = 0
    for idx in range(len(w)):
        if w[idx]!=t[idx]:
            count+=1
    isDiff = True if count==1 else False
    return isDiff




def solution(begin, target, words):
    visited=[0]*len(words)
    n = len(words)
    answer = float("inf")
    def dfs(dept,begin):
        nonlocal answer
        if begin == target:
            ## print("end", begin, dept)
            answer= min(answer, dept)
            return
        for idx in range(n):
            if not(visited[idx]):
                visited[idx]=1
                if diff(begin, words[idx]):
                    dfs(dept+1, words[idx])
                visited[idx]=0
            
    dfs(0, begin)
    answer = 0 if answer==float("inf") else answer
        
    return answer