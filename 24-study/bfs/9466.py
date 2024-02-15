## 시간 초과

import sys
from collections import deque


input = sys.stdin.readline
T = int(input())


def group(idx, arr):
    lst = []
    while (idx not in lst):
        lst.append(idx)
        idx = arr[idx]
    return lst

for _ in range(T):
    n = int(input())
    arr = [0]+list(map(int, input().split()))
    visited = [0]*(n+1)
    inGroup = []
    for idx in range(1, n+1):
        if not(visited[idx]):
            result = group(idx, arr)
            if idx == arr[result[-1]]:
                for i in result:
                    visited[i]=1
    print(n-sum(visited))