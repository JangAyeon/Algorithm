import sys
input = sys.stdin.readline

a,b,c = map(int, input().split())

def mul(n,m):
    if m==1:
        return n%c
    temp = mul(n,m//2)
    if m%2==0:
        return temp*temp%c
    else:
        return temp*temp*n%c
        
        
print(mul(a,b))