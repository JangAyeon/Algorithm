#code before lecture
import sys
sys.stdin=open("in5.txt","r")


c,n=map(int,input().split())
arr=[]
res=[]
for i in range(n):
    arr.append(int(input()))

def DFS(L,w):
    if w>c:
        return
    else:
        if L==n:
            res.append(w)
            return
        else:
            res.append(w)
            DFS(L+1,w+arr[L])
            DFS(L+1,w)

DFS(0,0)
print(max(res))