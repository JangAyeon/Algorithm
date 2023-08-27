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