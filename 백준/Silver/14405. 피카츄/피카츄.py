import sys
from collections import deque
input = sys.stdin.readline

words = list(input())
stack = []
flag = True
for w in words:
    stack.append(w)
    s = "".join(stack)
    ##print(stack, s)
    if len(stack)==2: 
        
        if s in ["pi", "ka"]:
            stack = []
        elif s !="ch":
            flag = False
            break

    elif len(stack)==3:
        if s!="chu":
            flag = False
            break
        else:
            stack = []

if flag:
    print("YES")
else:
    print("NO")
      

