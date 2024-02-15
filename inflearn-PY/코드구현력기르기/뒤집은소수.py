#code before lecture

N=int(input())
M=list(input().split())

def reverse(x):
    return (int(x[::-1]))

def isPrime(x):

    cnt=[0]*(x+1)
    for i in range(2,x+1):
        if cnt[i]==0:
            for j in range(i+i,x+1,i):
                cnt[j]+=1
    

    if x!=0 and x!=1 and cnt[x]==0: #0과 1인 경우 빼야함
        return True
    else:
        return False

for x in M:
    rev_x=reverse(x)
    if isPrime(rev_x):
        print(rev_x,end=" ")


#code from lecture
def reverse(x):
    res=0
    while x>0:
        t=x%10
        res=res*10+t
        x//=10
    return res

def isPrime(x):
    if x==1:
        return False
    for i in range(2,x//2+1):
        if x%i==0:
            return False
    else:
        return True

n=int(input())
a=list(map(int,input()))
for x in a:
    tmp=reverse(x)    
    if isPrime(tmp):
        print(tmp, end=" ")
    

