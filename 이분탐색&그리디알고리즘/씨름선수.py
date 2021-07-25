#code before lecture

n=int(input())
arr=[]
for _ in range(n):
    height,weight=map(int,input().split())
    arr.append((height,weight))


cnt=0
for i in range(n):
    #print("i:",i)
    for j in range(n):
        #print("j: ",j,end=" ")
        if ((arr[i][0]<arr[j][0]) and (arr[i][1]<arr[j][1])):
            #print(": 미달")
            break
        if (j==(n-1)):
            cnt+=1
    

print(cnt)

