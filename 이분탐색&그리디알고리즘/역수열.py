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


#code from lecture
n=int(input())
a=list(map(int,input().split()))
seq=[0]*n
for i in range(n):
    for j in range(n):
        if a[i]==0 and seq[j]==0: 
            #자기 자리 찾음 
            #앞에 더 큰 수 갯수 만족 & 빈공간 찾음
            seq[j]=(i+1)
            break
        elif seq[j]==0:
            #아직 자기 자리 못 찾음
            #자신보다 큰 숫자 자리 확보 아직 다 못함
            a[i]-=1

for x in seq:
    print(x,end=" ")
    



