# 문제 : https://www.acmicpc.net/problem/15665

import sys
input= sys.stdin.readline
n,m = map(int, input().split())
arr=sorted(list(set(map(int, input().split()))))
print(n,m,arr)
ans=[]


def solution(cnt):
    if cnt==m:
        print(*ans)
        return
    cnt+=1
    for i in arr:
        ans.append(i)
        solution(cnt)
        ans.pop()

solution(0)