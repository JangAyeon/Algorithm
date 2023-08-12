import sys
import heapq
input = sys.stdin.readline

n,k = map(int,input().split())
gem = [list(map(int,input().split())) for _ in range(n)]
bag = [int(input()) for _ in range(k)]
gem.sort()
bag.sort()

Q =[]
answer = 0
for b_weight in bag:
    while gem and gem[0][0]<=b_weight:
        heapq.heappush(Q, -heapq.heappop(gem)[1])
    if Q: 
        answer -= heapq.heappop(Q)

print(answer)