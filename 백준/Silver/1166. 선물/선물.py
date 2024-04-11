import sys
input = sys.stdin.readline
import math

n,l,w,h = map(int, input().split())
answer = -1


start = 0
end = min([l,w,h])
for i in range(100):
    mid = (start+end)/2
    count = int(l/mid)*int(w/mid)*int(h/mid)
    ## print(answer, mid, start,end)
    
    if count>=n:
        answer = mid
        start = mid
    else:
        end = mid

print(answer)