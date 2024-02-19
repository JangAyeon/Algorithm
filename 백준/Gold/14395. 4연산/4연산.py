import sys
input = sys.stdin.readline
from collections import deque

n,m = map(int,input().split())
MAX_ = 10**9
visited = []
ans = []
cmds = ['*', '+', '-', '/']
cmds.sort()
def calc(num, cmd):
    if cmd=="+":
        return num+num
    elif cmd=="-":
        return num-num
    elif cmd=="*":
        return num*num
    else:
        return num/num


def bfs():
    global ans
    que = deque()
    que.append([n,[]])
    while que:
        num, process = que.popleft()
        for idx in range(4):
            if num==0 and cmds[idx]=="/":
                continue
            x = calc(num, cmds[idx])
    
            
            if x==m:
                #print(x, process+[cmds[idx]])
                ans.append(process+[cmds[idx]])
                return
   
            if x<=MAX_ and x not in visited:
                que.append([x, process+[cmds[idx]]])
                visited.append(x)

if n==m:
    print(0)
else:
    bfs()
    if not(ans):
        print(-1)
    else:
        ans.sort()
        answer = "".join(ans[0])
        print(answer)

