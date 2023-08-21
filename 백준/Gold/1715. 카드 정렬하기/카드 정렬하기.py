import sys
input = sys.stdin.readline
from heapq import heappush, heappop

n = int(input())
heap = []
for _ in range(n):
    num = int(input())
    heappush(heap, num)
answer = 0

while len(heap)!=1:
    num1 = heappop(heap)
    num2 = heappop(heap)
    temp = num1+num2
    answer+=temp
    #print(answer, temp, heap)
    heappush(heap, temp)
    
print(answer)

