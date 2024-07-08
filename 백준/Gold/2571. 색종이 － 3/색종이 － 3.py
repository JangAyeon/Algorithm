import sys
input = sys.stdin.readline

n = int(input())
m = 101
board = [[0 for _ in range(m)] for _ in range(m)]
for _ in range(n):
    r,c = map(int, input().split())
    for dr in range(10):
        for dc in range(10):
            board[r+dr][c+dc]=1


for r in range(m):
    for c in range(m):
        if board[r][c]:
            board[r][c]+=board[r][c-1]

"""
for i in board:
    print(i[3:30])

"""


answer = 0
for c in range(m):
    for r in range(m):
        width = m
        for nr in range(r, m):
            width = min(width, board[nr][c])
            answer = max(answer, width*(nr-r+1))
print(answer)



