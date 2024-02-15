# 참고 풀이 : https://velog.io/@yje876/python%EB%B0%B1%EC%A4%80%EB%B6%84%ED%95%A0%EC%A0%95%EB%B3%B5-1780-%EC%A2%85%EC%9D%B4%EC%9D%98-%EA%B0%9C%EC%88%98

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