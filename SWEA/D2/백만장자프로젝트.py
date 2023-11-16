# https://swexpertacademy.com/main/code/problem/problemDetail.do

T = int(input())
ans=[]
for idx in range(T):
    k = int(input())
    arr = list(map(int, input().split()))
    b = 0
    p = arr.pop()
    while arr:
        curr = arr.pop()
        if curr<p:
            b+=p-curr
        else:
            p=curr
        
    ans.append([idx+1,b])
    
for idx, value in ans:
    print("#"+str(idx), value)
        
    