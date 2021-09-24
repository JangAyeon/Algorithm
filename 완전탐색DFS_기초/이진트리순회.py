#code before lecture

def pre(a):
    if a>(n+1):
        for i in range(1,len(dp)):
            if dp[i]==1:
                print(i, end=" ")
    else:
        dp[a]=1
        left=a*2
        right=a*2+1
        pre(left)
        dp[a]=0
        pre(right)



if __name__=="__main__":
    n=int(input())
    print(n)
    dp=[0]*(n+1)
    pre(1)


#code from lecture
def pre(v): #전위 순회
    if v>7:
        return
    else:
        print(v, end=" ") #방문
        pre(v*2) #왼쪽 자식
        pre(v*2+1) #오른쪽 자식

def mid(v):
    if v>7:
        return
    else:
        mid(v*2) #왼쪽 자식
        print(v, end=" ") #방문
        mid(v*2+1) #오른쪽 자식

def post(v):
    if v>7:
        return 
    else:
        post(v*2) #왼쪽 자식
        post(v*2+1) #오른쪽 자식
        print(v, end=" ") #방문


if __name__=="__main__":
    pre(1) #전위
    print()
    mid(1) #중위 
    print()
    post(1) #후위
    print()