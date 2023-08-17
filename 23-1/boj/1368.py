import sys
input = sys.stdin.readline
from heapq import heappop, heappush

n = int(input())
parent = [i for i in range(n+1)]
heap = []

for i in range(1, n+1):
    cost = int(input())
    heappush(heap,[cost, 0, i])
    
for i in range(1, n+1):
    costs = list(map(int, input().split()))
    for j in range(1, n+1):
        heappush(heap, [costs[j-1], i, j])

def find_parent(x):
    if parent[x]!=x:
        parent[x] = find_parent(parent[x])
    return  parent[x]
    
def union(a,b):
    a = find_parent(a)
    b = find_parent(b)
    
    if a<b:
        parent[a] = b
    else:
        parent[b] = a
        
answer = 0
while heap:
    cost, a,b=heappop(heap)
    if find_parent(a)!=find_parent(b):
        union(a,b)
        answer+=cost
        
print(answer)