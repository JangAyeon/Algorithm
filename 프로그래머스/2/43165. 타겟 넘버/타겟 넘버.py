def solution(numbers, target):
    answer = []
    N = len(numbers)
    
    def dfs(idx, total):
        if(idx ==N):
            if(total==target):
                answer.append(1)
            return
        dfs(idx+1, total+numbers[idx])
        dfs(idx+1, total+numbers[idx]*(-1))
    dfs(0,0)
    return len(answer)