def solution(numbers):
    n = len(numbers)
    answer = [-1] * (n)
    stack=[]
    for idx,v in enumerate(numbers):
        while stack and numbers[stack[-1]]<v:
            i = stack.pop()
            answer[i]=v
        stack.append(idx)
    return answer