import sys
input=sys.stdin.readline


N,M,K=map(int, input().split())
#print(N,M,K)

def Mul(n,m):
    if m==1:
        return n%K
    else:
        tmp=Mul(n,m//2)
        if m%2==0:
            return tmp*tmp%K
        else:
            return tmp* tmp*n%K

print(Mul(N,M))