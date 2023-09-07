import sys
input = sys.stdin.readline

n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]


area = {-1:0, 0:0, 1:0}


def divided(row, col, n):
    curr = graph[row][col]
    
    for i in range(row, row+n):
        for j in range(col, col+n):
            if graph[i][j]!=curr:
                gap = n//3
                
                divided(row, col, gap)
                divided(row, col+gap, gap)
                divided(row, col+2*gap, gap)
                
                divided(row+gap, col, gap)
                divided(row+gap, col+gap, gap)
                divided(row+gap, col+2*gap, gap)
                
                divided(row+2*gap, col, gap)
                divided(row+2*gap, col+gap, gap)
                divided(row+2*gap, col+2*gap, gap)
                return
            
    area[curr]+=1
    return
            #print(i,j)
        #print("==========")
    #print("======End========")
divided(0,0,n)

for i in area.values():
    print(i)