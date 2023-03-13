import sys

N=int(sys.stdin.readline())
board = [0] * N
row =[False] * N
diagA=[False] * (N*2-1)
diagB=[False] * (N*2-1)

cnt=0
def getQueen(i, outer=True):
        global N
        if outer :
            if N%2 == 1 :
                repeat = N//2 +1
            else :
                repeat = N//2
        else :
            repeat = N

        for j in range(repeat):
            if(not row[j] and not diagA[i+j] and not diagB[i-j+(N-1)]):
                board[i] = j
                if i ==(N-1):
                    global cnt
                    cnt+=1
                else:
                    row[j]=diagA[i+j]=diagB[i-j+(N-1)]=True
                    getQueen(i+1, False)
                    row[j]=diagA[i+j]=diagB[i-j+(N-1)]=False
                if outer and j == N//2-1 :
                        cnt *= 2

getQueen(0)
print(cnt)

# 아직 공부 안 함 그냥 돌아가는 코드 찾음