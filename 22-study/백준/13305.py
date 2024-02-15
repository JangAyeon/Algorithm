import sys
input = sys.stdin.readline

N = int(input())
dist =  list(map(int, input().split()))
cost = list(map(int, input().split()))

#print(N, dist, cost)
min_cost=cost[0]
res = 0
for i in range(N-1):
    if min_cost>=cost[i]:
        #print(cost[i], dist[i])
        min_cost=cost[i]
    res+=min_cost*dist[i]
print(res)