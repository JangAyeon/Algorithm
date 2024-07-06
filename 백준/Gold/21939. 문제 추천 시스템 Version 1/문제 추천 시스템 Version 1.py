import sys
input = sys.stdin.readline
from heapq import heappop, heappush, heapify

"""
recommend 1 : 가장 어려운 문제 가장 큰 번호
recommend -1 : 가장 쉬운 문제 가장 작은 번호 
add P L : L 난이도 문제 번호 P ()
solved P : 문제번호 P 제거
"""

n = int(input())
maxHeap = []
minHeap = []
problems = []
for _ in range(n):
    p, l = map(int, input().split()) # 문제 번호, 난이도
    heappush(maxHeap, (-l, -p)) ## 난이도, 문제 번호
    heappush(minHeap, (l, p))
    problems.append(p)

## 난이도 2 (1), 난이도 1 (2)
###print(problems, hard, easy)
m = int(input())
for _ in range(m):
    cmds = list(input().split())
    cmd = cmds[0]
    numbers = list(map(int, cmds[1:]))
    ###print(cmd, numbers)
    if cmd=="recommend":
        if numbers[0]==1:
            print(-(maxHeap)[0][1])
        else:
            print((minHeap)[0][1])
    elif cmd=="add": ## 문제번호, 난이도
        heappush(maxHeap, (-numbers[1], -numbers[0]))
        heappush(minHeap, (numbers[1], numbers[0]))
    elif cmd=="solved":
        if numbers[0]==minHeap[0][1]:
            heappop(minHeap)
        elif numbers[0]==-maxHeap[0][1]:
            heappop(maxHeap)
        

