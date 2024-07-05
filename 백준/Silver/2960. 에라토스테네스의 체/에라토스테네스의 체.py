import sys
input = sys.stdin.readline

n,m = map(int, input().split())
visited =[0 for _ in range(n+1)]
count=0
flag = False
answer = 0
for i in range(2, n+1):
    ##print("i",i)
    for j in range(i, n+1,i):
        ##print(count, j)
        if not(visited[j]):
            count+=1
            visited[j]=1
            if count==m:
                answer = j
print(answer)


