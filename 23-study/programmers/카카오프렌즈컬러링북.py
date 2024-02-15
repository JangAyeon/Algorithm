from collections import deque

dr = [-1,1,0,0]
dc = [0,0,-1,1]


def bfs(row, col,answer,picture, visited, m,n):
    count = 1
    que = deque()
    que.append([row,col])
    visited[row][col]=True
    color = picture[row][col]
    while que:
        row, col = que.popleft()
        for i in range(4):
            nr,nc = row+dr[i], col+dc[i]
            if not(0<=nr<m and 0<=nc<n):
                continue
            if not visited[nr][nc] and picture[nr][nc]==color:
                que.append([nr, nc])
                visited[nr][nc]=True
                count+=1
                
    answer[0]+=1
    answer[1] = max(answer[1], count)
    return answer, visited
    

def solution(m,n,picture):
    ## 그림 영역 갯수, 가장 큰 칸의 칸 수
    answer = [0,0]
    visited = [[False]*n for _ in range(m)]
    for row in range(m):
        for col in range(n):
            if picture[row][col]!=0 and not visited[row][col]:
                answer,visited = bfs(row, col, answer,picture, visited, m,n)
                
    return answer
    
input1=[2, 2, [ [ 1, 1 ], [ 0, 1 ] ]]
input2 = [6, 4, [ [ 1, 1, 1, 0 ], [ 1, 2, 2, 0 ], [ 1, 0, 0, 1 ], [ 0, 0, 0, 1 ], [ 0, 0, 0, 3 ], [ 0, 0, 0, 3 ] ]]
input3 =[6, 4, [ [ 1, 0, 0, 1 ], [ 1, 0, 0, 1 ], [ 1, 0, 0, 1 ], [ 1, 0, 0, 1 ], [ 1, 0, 0, 1 ], [ 1, 1, 1, 1 ]]] 
input4=[1, 1, [ [ 0 ] ]]
input5 = [4, 4, [[ 1, 1, 1, 1 ], [ 1, 4, 1, 1 ], [ 1, 3, 2, 1 ], [ 1, 1, 1, 1 ] ]]
input6= [6, 4, [[1, 1, 1, 0], [1, 2, 2, 0], [1, 0, 0, 1], [0, 0, 0, 1], [0, 0, 0, 3], [0, 0, 0, 3]]]

inputs=[input1, input2, input3, input4, input5,input6]

for m,n,picture in inputs:
    print(solution(m,n,picture))
    
"""
[2, 2, [ [ 1, 1 ], [ 0, 1 ] ]]
ans: [1,3]
"""

"""
[6, 4, [ [ 1, 1, 1, 0 ], [ 1, 2, 2, 0 ], [ 1, 0, 0, 1 ], [ 0, 0, 0, 1 ], [ 0, 0, 0, 3 ], [ 0, 0, 0, 3 ] ]]
ans: [4,5]
"""

"""
[6, 4, [ [ 1, 0, 0, 1 ], [ 1, 0, 0, 1 ], [ 1, 0, 0, 1 ], [ 1, 0, 0, 1 ], [ 1, 0, 0, 1 ], [ 1, 1, 1, 1 ]]] 
ans: [1,14]
"""

"""
[1, 1, [ [ 0 ] ]
ans: [0, 0]
"""

"""
[4, 4, [[ 1, 1, 1, 1 ], [ 1, 4, 1, 1 ], [ 1, 3, 2, 1 ], [ 1, 1, 1, 1 ] ]]
ans: [4, 13]
"""

"""
[6, 4, [[1, 1, 1, 0], [1, 2, 2, 0], [1, 0, 0, 1], [0, 0, 0, 1], [0, 0, 0, 3], [0, 0, 0, 3]]]
ans: [4,5]
"""
