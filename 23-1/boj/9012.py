import sys
input = sys.stdin.readline

T = int(input())

def check(arr):
    stack = []
    for i in arr:
        #print(i,stack)
        if i=="(":
            stack.append(i)
        else:
            if stack:
                stack.pop()
            else:
                return False
           
    if len(stack)==0:
        return True
    else:
        return False

for _ in range(T):
    arr = list(input().strip())
            
    if check(arr):
        print("YES")
    else:
        print("NO")