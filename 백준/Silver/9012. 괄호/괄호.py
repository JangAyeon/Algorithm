import sys
input = sys.stdin.readline

n = int(input())


def isValid(arr):
    stack = []
    for i in arr:
        if i =="(":
            stack.append("(")
        else:
            if stack:
                stack.pop()
            else:
                return False
                
    if stack:
        return False
    else:
        return True
        
for _ in range(n):
    arr = list(input().strip())
    if isValid(arr):
        print("YES")
    else:
        print("NO")