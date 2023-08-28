import sys
input = sys.stdin.readline

graph = [list(map(int, input().split())) for _ in range(9)]
zeros = [[row, col] for col in range(9) for row in range(9) if graph[row][col]==0]

def check_row(i, col):
    for row in range(9):
        if graph[row][col]==i:
            return False
    return True
    
def check_col(i, row):
    for col in range(9):
        if graph[row][col]==i:
            return False
    return True
    
def check_rect(i, row, col):
    row = row//3*3
    col = col//3*3
    
    for dr in range(3):
        for dc in range(3):
            if graph[row+dr][col+dc]==i:
                return False
                
    return True
    
def dfs(count):
    if count==len(zeros):
        for row in graph:
            print(*row)
        exit()
        
    row, col = zeros[count]
    
    for i in range(1,10):
        if check_row(i, col) and check_col(i, row) and check_rect(i, row, col):
            graph[row][col]=i
            dfs(count+1)
            graph[row][col]=0
            
dfs(0)