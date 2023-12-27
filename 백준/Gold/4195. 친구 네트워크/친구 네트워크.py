

import sys
input = sys.stdin.readline

def union(a,b):
    a = find(a)
    b = find(b)
    if a==b:
        return network[a]
    parents[b] = a
    network[a] = network[a] + network[b]
    return network[a]
    
def find(k):
    if k != parents[k]:
        parents[k] = find(parents[k])
    return parents[k]

for _ in range(int(input())):
    parents = dict()
    network = dict()
    for _ in range(int(input())):
        a,b = input().rstrip().split()
        if parents.get(a) == None:
            parents[a] = a
            network[a] = 1
        if parents.get(b) == None:
            parents[b] = b
            network[b] = 1
            
        print(union(a,b))