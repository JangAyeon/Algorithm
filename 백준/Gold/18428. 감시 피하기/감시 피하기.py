import sys
from itertools import combinations
input = sys.stdin.readline

n = int(input())
graph = [input().split() for _ in range(n)]
teachers = []
blanks = []

find = False
for i in range(n):
    for j in range(n):
        if graph[i][j]=="T":
            teachers.append([i,j])
        elif graph[i][j]=="X":
            blanks.append([i,j])
            
def watch(r,c,idx):
    
    # 위
    if idx == 0:
        while 0<=r<n:
            if graph[r][c]=="O":
                return False
            elif graph[r][c]=="S":
                return True
            r-=1
        
    # 아래
    elif idx ==1:
        while 0<=r<n:
            if graph[r][c]=="O":
                return False
            elif graph[r][c]=="S":
                return True
            r+=1
        
    # 왼쪽
    elif idx==2:
        while 0<=c<n:
            if graph[r][c] =="O":
                return False
            elif graph[r][c] =="S":
                return True
            c-=1
        
    # 오른쪽
    elif idx==3:
        while 0<=c<n:
            if graph[r][c]=="O":
                return False
            elif graph[r][c]=="S":
                return True
            c+=1
    return False
            
def process():
    for r,c in teachers:
        for i in range(4):
            if watch(r,c,i):
                return True
    return False
            
# 장애물 설치할 3가지 장소 
for locations in combinations(blanks,3):
    for r, c in locations:
        graph[r][c]="O"
    if not process():
        find = True
        break
    for r,c in locations:
        graph[r][c] = "X"
    
if find:
    print("YES")
else:
    print("NO")