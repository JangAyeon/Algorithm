# 친구와 친구의 친구까지 초대
import sys
input = sys.stdin.readline
from collections import deque

# 리스트 길이 
n = int(input())


graph = [list(map(int, input().split())) for _ in range(n)]



    
def search(start, end):
    visited= [False]*(n+1)
    que = deque()
    que.append(start)
    while que:
        node = que.popleft()
        for col, v in enumerate(graph[node]):
            #print(node, col, end)
            if v ==0:
                continue
            if not visited[col]:
                que.append(col)
                visited[col] = True
                if col==end:
                    return True

    return False
            
#print("==========")
for i in range(n):
    for j in range(n):
        if search(i,j):
            print(1,end=" ")
        else:
            print(0, end=" ")
    print()

"""
in:
5
0 1 0 1 0
0 0 1 0 0
0 0 0 0 1
0 0 1 0 0
0 0 0 0 0
    
out:
0 1 1 1 1
0 0 1 0 1
0 0 0 0 1
0 0 1 0 1
0 0 0 0 0
"""