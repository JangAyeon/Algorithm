import sys
input = sys.stdin.readline



n = int(input())
heap = []
parent = [i for i in range(n+1)]

for r in range(n):
    row =  list(map(int, input().split()))
    for c in range(len(row)):
        heap.append([row[c],r,c])

def find(node):
    if node!=parent[node]:
        parent[node]=find(parent[node])
    return parent[node]

def union(a,b):
    a,b = find(a), find(b)
    if a<b:
        parent[a] = b
    else:
        parent[b] = a
    

answer = 0
heap.sort(key=lambda x : x[0])

for cost, start,end in heap:
    if find(start)!=find(end):
        union(start, end)
        answer +=cost

print(answer)
