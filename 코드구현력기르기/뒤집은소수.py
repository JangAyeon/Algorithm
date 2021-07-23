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

    
    

