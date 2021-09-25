




def DFS(a):

    if a==(n):
        res0=0
        res1=0
        for x in range(len(dp)):
            
            if dp[x]==1:
                
                res0=+arr[x]
                print("1: ",arr[x], res0,end=",",)
            else:
                print("0: ",arr[x],res1,end=",")
                res1=+arr[x]
        if res1==res0:
            print("#sum=",res1,res0)
            print("성공")
        else:
            print("#sum1=",res1,"sum0=",res0)
            print("실패")

    else:
        dp[a]=1
        DFS(a+1)
        dp[a]=0
        DFS(a+1)



if __name__=="__main__":
    n=int(input())
    arr=list(map(int,input().split()))
    dp=[0]*(n)

    DFS(0)



