import sys
input = sys.stdin.readline

idx = 0

while True:
    stack = []
    count=0
    arr = list(input().strip())

    if "-" in arr:
        break 

    for i in arr:
        if i=="{":
            stack.append(i)
        else:
            if stack:
                stack.pop()
            else:
                count+=1
                stack.append(i)

    idx+=1
    count+=len(stack)//2
    print(str(idx)+". "+str(count))



