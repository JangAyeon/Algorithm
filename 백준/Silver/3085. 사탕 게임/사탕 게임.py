import sys
input = sys.stdin.readline

n = int(input())
board = list(list(input()) for _ in range(n))
answer = 0


def check():
    global answer
    for i in range(n):
        count=1
        ## 오른쪽으로 검사 
        for j in range(1,n):
            if board[i][j]==board[i][j-1]:
                count+=1
                answer = max(answer, count)
            else:
                count = 1
        count = 1
        ## 아래로
        for j in range(1,n):
            if board[j][i]==board[j-1][i]:
                count+=1
                answer = max(answer, count)
            else:
                count=1

for i in range(n):
    for j in range(n):
        ## 오른쪽
        if j+1<n:
            ## 바꾸고
            board[i][j], board[i][j+1] =  board[i][j+1],  board[i][j]
            check()
            ## 원래대로
            board[i][j], board[i][j+1] =  board[i][j+1],  board[i][j]
        ## 아래로
        if i+1<n:
            board[i][j], board[i+1][j] = board[i+1][j], board[i][j]
            check()
            board[i][j], board[i+1][j] = board[i+1][j], board[i][j]
            
            
print(answer)