#https://www.acmicpc.net/problem/2630


import sys
input=sys.stdin.readline

N=int(input())
arr=[list(map(int, input().split())) for _ in range(N)]
#print(N,arr)
res=[]

def split(n,x,y):
    color=arr[x][y]
    #print(color)
    for i in range(x,x+n):
        for j in range(y,y+n):
            if arr[i][j]!=color:
                split(n//2,x,y)
                split(n//2,x,y+n//2)
                split(n//2,x+n//2,y)
                split(n//2,x+n//2,y+n//2)
                return
    if color==0:
       res.append(0)
    else:
       res.append(1)

split(N,0,0)
print(res.count(0))
print(res.count(1))
