import sys
input = sys.stdin.readline

n,m = map(int, input().split())
lst = list(map(int, input().split()))


h = -float("inf")

def getHeight(height):
    temp = 0
    for i in lst:
        cut = i- height
        if cut>0:
            temp+=cut
    return temp


def bisect(start, end):
    global h
    if start>end:
        return
    height = (start+end)//2
    total = getHeight(height)
    ###print(total, height)
    if m<=total:
        h = height
        bisect(height+1, end)

    else:
        bisect(start,height-1)

bisect(0, max(lst))
print(h)