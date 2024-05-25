"""
입력[2, 2, 3, 1, 5]
출력[3, 2, 1, 1, 0]
"""

def solution(prices):
    n = len(prices)
    stack = []
    answer = [-1]*(n)
    stack=[0]
    for i in range(1,n):
        price = prices[i]
        while stack and prices[stack[-1]]>prices[i]:
            x = stack.pop()
            answer[x] = i-x
        stack.append(i)
            
    while stack:
        x = stack.pop()
        answer[x] = i-x

    return answer