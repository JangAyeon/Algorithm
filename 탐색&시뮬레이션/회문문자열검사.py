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


#code from lecture (1)
n=int(input())
for i in range(n):
    s=input()
    s=s.upper()
    size=len(s)
    for j in range(size//2):
        if s[j]!=s[-(1+j)]:
            print("#%d NO" %(i+1))
            break
    else:
        print("#%d YES" %(i+1))


#code from lecture (2)
n=int(input())
for i in range(n):
    s=input()
    s=s.upper()
    if s==s[::-1]:
        print("#%d YES" %(i+1))
    else:
        print("#%d NO" %(i+1))