import sys
input = sys.stdin.readline

a1,a0 = map(int, input().split())
c=int(input())
n0 = int(input())

k=(a1*n0+a0)/(c*n0)
if(k<=1 and a1<=c):
    print( 1)
else:
    print(0)
    