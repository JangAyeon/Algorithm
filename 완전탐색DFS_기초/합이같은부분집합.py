
#code before lecture
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

#code from lecture

def DFS(L,sum):
    if sum>totall//2: #부분집합의 합이 이미 전체 합의 절반을 넘어버린 경우 고려 X
        return
    if L==n:
        if sum==(total-sum): #또 다른 부분 집합
            print("YES")
            sys.exit(0) #프로그램 전체 종료
    else:
        DFS(L+1,sum+a[L]) #Level, 부분 집합에 값 더하기
        DFS(L+1,sum)


if__name__=="__main__":
    n=int(input())
    a=list(map(int,input().split()))
    total=sum(a)
    DFS(0,0)