import sys
input = sys.stdin.readline

n,m = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort(key=lambda x: (x%10,x))
##print(n,m,arr)

def cutting(length):
    cut = length//10
    piece = length//10
    if not(length%10):
        cut-=1
    return piece, cut
total_c=0
total_p=0
for length in arr:
    p,c =cutting(length)
    ##print("***",p,c)
    if total_c+c<=m:
        total_p+=p
        total_c+=c                       
    else:
        total_p+=(-total_c+m)
        total_c=m

        break
print(total_p)