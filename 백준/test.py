n = int(input())
b = input().split()
visited = [False] * 10 # 0 ~ 9
mx,mn ="",""

def possible(i,j,k):
    if k=="<":
        return i<j
    elif k==">":
        return i>j

def solution(count, s):
    global mn,mx
    if count == n+1:
        if len(mn)==0:
            mn=s
        else:
            mx=s
        return
    
    for i in range(10): # 0~9
        if not visited[i]:
            if count == 0 or possible(s[-1], str(i), b[count-1]):
                visited[i]=True
                solution(count+1, s+str(i))
                visited[i]=False


solution(0,"")
print(mx)
print(mn)