import sys
input = sys.stdin.readline

arr = list(input().strip())
n = len(arr)
str_ = list(input().strip())
m = len(str_)

start = 0
answer = 0
while(start+m-1<len(arr)):
    chunk = arr[start:start+m]
    if chunk==str_:
        start+=m
        answer+=1
    else:
        start+=1
    
print(answer)