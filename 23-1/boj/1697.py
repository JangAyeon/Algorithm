import sys
from collections import deque
input = sys.stdin.readline

n,m = map(int, input().split())
arr = [-1]*(100000+1)
arr[n] = 0
que = deque([n])

def create_idx(x,m):
    arr = []
    if 0<=x-1<=100000:
        arr.append(x-1)
    if 0<=x+1<=100000:
        arr.append(x+1)
    if 0<=2*x<=100000:
        arr.append(2*x)
    return arr


while que:
    x = que.popleft()
    for idx in create_idx(x,m):
        if arr[idx]==-1:
            arr[idx]=arr[x]+1
            que.append(idx)
            
print(arr[m])

