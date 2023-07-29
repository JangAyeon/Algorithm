import sys
input = sys.stdin.readline
n = int(input())

for _ in range(n):
    arr = list(input().strip())
    l=[]
    r=[]
    
    for i in arr:
        #print(l,r,i)
        if i == "<":
            if l:
                r.append(l.pop())
        elif i == ">":
            if r:
                l.append(r.pop())
        elif i == "-":
            if l: l.pop()
        else:
            l.append(i)

    print("".join(l+list(reversed(r))))