
import sys
sys.stdin=open("in5.txt","r")

def DFS(a):

    if a==n:
        if sum(part)==(sum(arr)-sum(part)):
            res.append("YES")
        else:
            res.append("NO")

    else:
        part.append(arr[a])
        DFS(a+1)
        part.remove(arr[a])
        DFS(a+1)



if __name__=="__main__":
    n=int(input())
    arr=list(map(int,input().split()))
    part=[]
    res=[]
    DFS(0)

    if "YES" in res:
        print("YES")
    else:
        print("NO")


