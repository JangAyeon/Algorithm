import sys
input=sys.stdin.readline

n =  int(input().strip())
arr =[ [0]*(10) for _ in range(n+1)]
for i in range(1, 10):
    arr[1][i]=1

for i in range(2, n+1):
    print(i)
    for j in range(10):
        if j ==0:
            arr[i][j]=arr[i-1][1]
        elif j ==9:
            arr[i][j]=arr[i-1][8]
        else:
            arr[i][j]=arr[i-1][j-1]+arr[i-1][j+1]
print(arr)
print(sum(arr[-1]))