import sys
input = sys.stdin.readline

n = int(input())

def move(count, start, end, mid):
    if count==1:
        print(start, end)
    else:
        move(count-1,start, mid, end)
        print(start, end)
        move(count-1,mid, end, start)
    
print(pow(2,n)-1)
move(n, 1, 3, 2)