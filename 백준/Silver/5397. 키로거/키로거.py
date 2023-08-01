import sys
input = sys.stdin.readline
n = int(input())


for _ in range(n):
    arr = list(input().strip())
    l_stack = []
    r_stack = []
    for i in arr:
        if i == "<":
            if l_stack: r_stack.append(l_stack.pop())
        elif i == ">":
            if r_stack: l_stack.append(r_stack.pop())
        elif i=="-":
            if l_stack: l_stack.pop()
        else:
            l_stack.append(i)
            
    print("".join(l_stack+list(reversed(r_stack))))