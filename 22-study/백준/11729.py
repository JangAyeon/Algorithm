#https://www.acmicpc.net/problem/11729

import sys
input=sys.stdin.readline


N=int(input())
#print(N)


def hanoi(cnt,start, end, help):
    if cnt==1:
        print(start, end)
    else:
        
        hanoi(cnt-1, start,help,end) 
        #start : n-1개 (맨 위 원반 제외) -> 중간 지점
        print(start, end) 
        #start : 1개 (맨 밑 원반) -> goal 지점
        hanoi(cnt-1, help,end,start)
        #help : 중간 지점에 있는 나머지 원반 -> goal 지점

print(pow(2,N)-1)
hanoi(N,1,3,2)

