#code before lecture : fail
n=int(input())
a=list(map(int,input().split()))
arr=[0]*n

for i in range(len(a)):
    cnt=0
    print("i:",i+1)

    for j in range(len(a)):

        if (cnt==a[i]):
            if (cnt==0):
                arr[j]=(i+1)
                break
            if (arr[j+1]!=0):
                while(arr[j+1]!=0):
                    j+=1
            arr[j+1]=(i+1)
            break

        if arr[j]>(i+1) or arr[j]==0:
            cnt+=1
            print("cnt: ",cnt, "j: ",j,"arr[j]: ",arr[j])





    print("arr:",arr)
           

    

print(arr)

