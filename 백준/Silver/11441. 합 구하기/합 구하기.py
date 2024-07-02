import sys

input = sys.stdin.readline

n = int(input())
arr=[0]+list(map(int, input().split()))
for idx in range(1,n+1):
    arr[idx]+=arr[idx-1]
q = int(input())

for _ in range(q):
    a,b = map(int, input().split())
    print(arr[b]-arr[a-1])




