def checkRow():
    ans = 0
    for i in arr:
        temp = 0
        for j in i:
            if j==0:
                if isAble(temp, n):
                    ans+=1
                temp=0
            else:
                temp+=1
        if isAble(temp, n):
            ans+=1  
    return ans
    
def isAble(temp, n):
    if temp==n:
        return True
    else:
        return False

def checkCol():
    ans = 0
    for i in range(m):
        temp=0
        for r in arr:
            if r[i]==0:
                if isAble(temp, n):
                    ans+=1
                temp=0
            else:
                temp+=1
        if isAble(temp, n):
            ans+=1
    return ans

T = int(input())
for idx in range(T):
    m,n = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(m)]
    ans =0
    # print(checkRow(),checkCol())
    ans += (checkRow()+checkCol())
    print('#{0} {1}'.format(idx+1 ,ans))