import sys
input = sys.stdin.readline

arr = [list(map(int, input().split())) for _ in range(9)]
zero = [(x, y) for x in range(9) for y in range(9) if arr[x][y] == 0]

def check_x(n, x):
    for i in range(9):
        if arr[x][i] == n:
            return False
    return True


def check_y(n, y):
    for i in range(9):
        if arr[i][y] == n:
            return False
    return True


def check_rect(x, y, n):
    x = x // 3 * 3
    y = y // 3 * 3
    for i in range(3):
        for j in range(3):
            if arr[x + i][y + j] == n:
                return False
    return True


def dfs(cnt):
    if cnt == len(zero):
        for i in range(9):
            print(*arr[i])
        exit()
    x = zero[cnt][0]
    y = zero[cnt][1]
    for i in range(1, 10):
        if check_y(i, y) and check_rect(x, y, i) and check_x(i, x):
            arr[x][y] = i
            dfs(cnt + 1)
            arr[x][y] = 0 # i가 정답 아닐 수도 있으니 0으로!


#print(" ")
dfs(0)