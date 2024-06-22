def solution(arr):
    
    stack = [arr[0]]
    for num in arr:
        if stack and stack[-1]!=num:
            stack.append(num)
    ##print(stack)
    return stack