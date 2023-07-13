import sys
input = sys.stdin.readline

N = int(input())
dp = [[1,1] for _ in range(N+1)]

def default(N):
    print(1)
    print(N, 1)

def getDp(N):
    for i in range(4, len(dp)):
        temp = []
        #print("#",i)
        if (i%3==0):
            #print("3")
            temp.append([dp[i//3][0]+1,i//3])
        if (i%2==0):
            #print(2)
            temp.append([dp[i//2][0]+1,i//2])
        #print(1)
        temp.append([dp[i-1][0]+1,i-1]) 
        #print(temp, min(temp))
        dp[i] = min(temp)
    print(dp[N][0])

def printDp(N):
    idx= N
    print(N, end=" ")
    while True:
        n = dp[idx][1]
        print(n, end=" ")
        idx = n
        if n == 1:
            break
            
       
if N == 2 or N==3:
    default(N)
elif N ==1:
    print(0)
    print(1)
else:
    getDp(N)
    #print(dp)
    printDp(N)
    