def solution(numbers):
    n = len(numbers)
    answer = [0 for _ in range(n)]
    stack=[0]
    for i in range(1,n):
        while stack and numbers[stack[-1]]<numbers[i]:
            answer[stack.pop()]=numbers[i]
        stack.append(i)
    while stack:
        answer[stack.pop()]=-1
        
    return answer