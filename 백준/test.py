n = int(input())
arr = input().split()
visited = [False] * 10 # 0~9
mn,mx="",""



def possible(i,j,k):
    if k=="<":
        return i<j
    elif k==">":
        return i>j
    
def solution(count, res):
    global mn,mx

    if count==n+1:
        if len(mn)==0:
            mn=res
        else:
            mx=res
        return

    for i in range(10): # 0 ~ 9
        if not visited[i]:
            if count ==0 or possible(res[-1], str(i), arr[count-1]):
                visited[i]=True
                solution(count+1, res+str(i))
                visited[i]=False


solution(0, "")
print(mx)
print(mn)

