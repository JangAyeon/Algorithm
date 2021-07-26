#code before lecture

n=int(input())

for i in range(n):
    str=input().lower()
    length=len(str)-1
    #print("i: ",i+1,":",str)
    for j in range(int(len(str)/2)):
        if str[j]!=str[length-j]:
            print("#",i+1," NO",sep="")
            break
    else:
        print("#",i+1," YES",sep="")


