#code before lecture

n=int(input())
arr=list(range(1,n+1))

for i in range(0,n):
    for j in range(n,i,-1): #역순 출력
        for x in arr[i:j]:
            print(x, end=" ")
        print()


#code from lecture
def DFS(a):
    if a==n+1:
        for i in range(1,len(ch)):
            if ch[i]==1:
                print(i, end=" ")
        print()
    else:
        ch[a]=1
        DFS(a+1)
        ch[a]=0
        DFS(a+1)
        
if __name__=="__main__":
    n=int(input())
    ch=[0]*(n+1)
    DFS(1)
