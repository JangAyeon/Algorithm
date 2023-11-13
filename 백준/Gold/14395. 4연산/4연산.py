from collections import deque

d = ['*', '+', '-', '/' ]
MAX_=int(1e9)
def calc(num, cmd):
    if cmd=="*":
        return num*num
    if cmd=="+":
        return num+num
    if cmd=="-":
        return num-num
    if cmd=="/":
        return num//num
        

def bfs(start, result):
    visited=[]
    ans=[]
    global t
    que = deque()
    que.append([start, result])
    while que:
        num, progress = que.popleft()
        for i in range(4):
            if num==0 and d[i]=="/":
                continue
            x = calc(num, d[i])
            # print(num,x, d[i],progress)
            if x==t:
                ans.append(progress+[d[i]])
                return ans
            if x<=MAX_ and x not in visited:
                visited.append(x)
                que.append([x, progress+[d[i]]])
    return ans     
    
s,t = map(int, input().split())
if s==t:
    print(0)
else:
    ans = bfs(s,[])
    if len(ans)!=0:
        ans.sort()
        print("".join(ans[0]))
    else:
        print(-1)

