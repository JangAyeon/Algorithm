#https://www.acmicpc.net/problem/1074
#https://castlerain.tistory.com/87

import sys
input=sys.stdin.readline

n, r, c = map(int, input().split())

# return : 1,2,3,4 (몇사분면인지 알려준다.)
def find_q(n, r, c):

    num = 2**(n-1)

    # 해당 함수는 몇사분면 위인지 확인?
    if (r < num) & (c < num): # 1사분면
        return 0
    elif (r < num) & (c >= num): # 2사분면
        return 1
    elif (r >= num) & (c < num): # 3사분면
        return 2
    else: # 4사분면
        return 3

def visit(n,r,c):
    if n==1:
        return find_q(n,r,c)
    q=find_q(n,r,c)
    size=2**(n-1)
    visited=size*size*q
    if q==0:
        return visited+visit(n-1,r,c)
    elif q==1:
        return visited + visit(n-1,r,c-size)
    elif q==2:
        return visited + visit(n-1, r-size,c)
    else:
        return visited + visit(n-1, r-size,c-size)
print(visit(n, r, c))

 

