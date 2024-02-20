import sys
from collections import deque


input = sys.stdin.readline
T = int(input())

def group(i, arr, visited):
    while not(visited[i]):
        visited[i]=True
        i = arr[i]
    return i


for _ in range(T):
    answer = 0
    n = int(input())
    arr = [0]+list(map(int, input().split()))
    visited = [False]*(n+1)
    
    for i in range(1, n+1):
        if not(visited[i]):
            if i == group(i, arr, visited):
                answer+=1
    #print(n, arr, visited)
    print(answer)