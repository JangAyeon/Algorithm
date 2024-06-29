import sys
input = sys.stdin.readline

n,m,k,h = map(int, input().split())
## (n,k) (m,h)

i = 0
while True:
    temp = k-h+n*i
    if temp//m>=0 and (temp//m==temp/m):
        print(k+i*n)
        break
    ##print(temp//m, temp/m)
    if i>1000:
        print(-1)
        break
    i+=1

