import sys
input = sys.stdin.readline

x,y,c = map(float, input().split())
start, end = 0, min(x,y)


def get_c(m):
    a = (x**2-m**2)**(1/2)
    b = (y**2-m**2)**(1/2)
    return a*b/(a+b)


result = 0 
while end-start>1e-4:
    mid = (start+end)/2
    if get_c(mid)>=c:
        start = mid
        result = mid
    else:
        end=mid

print("{}".format(round(result,4)))