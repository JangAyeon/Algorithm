import sys
input = sys.stdin.readline
arr = list(input().strip())
stack=[]
answer = 0

for idx in range(len(arr)):
    if arr[idx]==")":
        stack.pop()
        if arr[idx-1] == "(":
            answer+=len(stack)
        else:
            answer+=1
    else: # arr[idx] == "(":
        stack.append(idx)
        
print(answer)