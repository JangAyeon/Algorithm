# https://www.acmicpc.net/problem/18808



N, M, K = map(int, input().split())
board = [[0]*M for _ in range(N)]
stickers = []

def check(sticker, y, x):
    r, c= len(sticker), len(sticker[0])
    for i in range(r):
        for j in range(c):
            if sticker[i][j]==1 and board[y+i][x+j]==1:
                return False
    for i in range(r):
        for j in range(c):
            if sticker[i][j]==1:
                board[y+i][x+j]=1
    return True


def rotate(sticker):
    c, r = len(sticker), len(sticker[0])

    temp = [[0 for _ in range(c)] for _ in range(r)]
    for i in range(r):
        for j in range(c):
            temp[i][j] = sticker[c-1-j][i]

    return temp

for _ in range(K):
    r, c =map(int, input().split())
    temp = [list(map(int, input().split())) for _ in range(r)]
    stickers.append(temp)

for sticker in stickers:
    turn = 0
    flag = False
    while True:
        flag = False
        r, c = len(sticker), len(sticker[0])
        for y in range(N - (r-1)):
            for x in range(M - (c-1)):
                if check(sticker, y, x) is True:
                    flag = True
                    break
            if flag:
                break
        if flag:
            break
        else:
            if (turn == 4):
                break
            sticker = rotate(sticker)
            turn += 1

ans = 0
for i in range(N):
    for j in range(M):
        if board[i][j] ==1:
            ans+=1

print(ans)