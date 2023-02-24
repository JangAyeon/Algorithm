"""
# 15661번

import sys
input =sys.stdin.readline
from itertools import combinations 

n = int(input().strip())
arr = [list(map(int, input().split())) for _ in range(n)]
#print(n, arr)
idx = list(range(n))
ans = float("inf")


def getDiff(start, link):
    s_score,l_score = 0, 0
    for x,y in combinations(start, 2):
        s_score += arr[x][y]+arr[y][x]
    for x,y in combinations(link,2):
        l_score += arr[x][y]+arr[y][x]
    return abs(s_score - l_score)

for i in range(1, n//2+1):
    start = list(combinations(idx, i))
    link = list(combinations(idx, n-i))
    cnt = len(start)

    for i in range(cnt):
        ans = min(ans,getDiff(start[i], link[cnt-1-i]))

print(ans)


# 15665번
import sys
input  = sys.stdin.readline

n,m = map(int,input().split())
arr = sorted(set(list(map(int, input().split()))))
ans = []
#print(n,m,arr)

def solution(cnt):
    if cnt == m:
        print(*ans)
        return
    cnt+=1
    for i in arr:
        ans.append(i)
        solution(cnt)
        ans.pop()

solution(0)


# 2580번
import sys
input = sys.stdin.readline

arr = [list(map(int, input().split())) for _ in range(9)]
zero = [(x,y) for x in range(9) for y in range(9) if arr[x][y]==0]
#print(arr, zero)

def check_x(i,x):
    for y in range(9):
        if arr[x][y]==i:
            return False
    return True

def check_y(i,y):
    for x in range(9):
        if arr[x][y] == i:
            return False
    return True


def check_rect(i,x,y):
    x = x//3*3
    y = y//3*3
    for dx in range(3):
        for dy in range(3):
            if  arr[x+dx][y+dy]==i:
                return False
    return True

def dfs(cnt):
    if cnt == len(zero):
        for row in arr:
            print(*row)
        exit()
    x = zero[cnt][0]
    y = zero[cnt][1]
    for i in range(1,10):
        #조건에 맞는 경우
        if check_x(i,x) and check_y(i,y) and check_rect(i,x,y):
            #print("답")
            arr[x][y]=i
            dfs(cnt+1)
            arr[x][y]=0


dfs(0)
"""

# 1941

import sys
input = sys.stdin.readline
from collections import deque

arr = [ input().strip() for _ in range(5)]
dx = [1,-1,0,0]
dy = [0,0,1,-1]
cnt=0

def check_s(group):
    s_cnt = 0 
    for x,y in group:
        if arr[x][y]=="S":
            s_cnt+=1
    return False if s_cnt<4 else True

def check_adj(group):
    visited = [False]*7
    que = deque()
    que.append(group[0])
    visited[0]=True

    while que:
        x,y = que.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if (nx,ny) in group:
                idx = group.index((nx,ny))
                #print(idx)
                if not visited[idx]:
                    visited[idx]=True
                    que.append((nx,ny))
    return False if False in visited else True



def solution(level, start, group):
    global cnt
    if level == 7:
        #print( group,check_adj(group), check_s(group))
        if check_adj(group) and check_s(group):
            cnt+=1
        return
    for i in range(start, 25):
        solution(level+1, i+1, group+[divmod(i,5)])

solution(0,0,[])
print(cnt)