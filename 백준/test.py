
"""

def dfs(board, visited, i, j, sum, cnt):
    


def solution(board):
    answer = 0
    visited  = [0] * 1000000

    for i in range(5):
        for j in range(5):
            dfs(board,visited, i,j, board[i][j],0)
    
    return sum(visited)




if __name__ =="__main__":
    answer = 0
    board = [[0]*5 for _ in range(5)]

    for i in range(5):
        board[i] = list(map(int, input().split()))
    
    answer = solution(board)
    print(answer) 
"""


import sys
input = sys.stdin.readline

n,m =  map(int, input().split())
r,c,d =  map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]

dr = [-1,0,1,0]
dc=[0,1,0,-1]
count=1
graph[r][c]=-1 #첫번째 방문 처리

while graph[r][c]!=1:
    flag = False
    for _ in range(4):
        d = (d+3)%4
        nr,nc = r + dr[d], c+ dc[d]
        if graph[nr][nc]==0:
            graph[nr][nc]=-1
            flag = True
            r=nr
            c=nc
            count+=1
            break
    if not flag:
        r+=dr[d-2]
        c+=dc[d-2]
print(count)