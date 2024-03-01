"""
입력[2, 2, 3, 1, 5]
출력[3, 2, 1, 1, 0]
"""


def solution(prices):
    n = len(prices)
    answer = [0]*(n)
    stack = [0]
    
    for i in range(1, n):
        ## 가격이 떨어진 경우
        while stack and prices[stack[-1]]>prices[i]:
            p = stack.pop()
            answer[p] =i-p
        stack.append(i)

    while stack:
        j = stack.pop()
        answer[j] = n-1-j 
            
            
    return answer