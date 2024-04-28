import sys
input = sys.stdin.readline

n, k=map(int, input().split())
arr=list(map(int, input().split()))
sum_=[0]

for i in range(n):
    sum_.append(sum_[-1]+arr[i])


answer = -float("inf")
for i in range(k,n+1):
    num = sum_[i]-sum_[i-k]
    answer = answer if answer>=num else num
print(answer)