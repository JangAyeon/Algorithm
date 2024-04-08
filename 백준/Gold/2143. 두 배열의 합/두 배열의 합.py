import sys
input = sys.stdin.readline
from collections import Counter

m = int(input())
c = int(input())
arr1 = list(map(int, input().split()))
d = int(input())
arr2 = list(map(int, input().split()))
answer = 0

## 구간별 누적함
def partSum(arr,n):
    sum_ = []
    n = len(arr)
    for i in range(0,n):
        for j in range(i+1, n+1):
            sum_.append(sum(arr[i:j]))
    return sum_




        
    
sum1=Counter(partSum(arr1, c))
sum2=Counter(partSum(arr2, d))
## print(sum1, sum2)

for i in sum1.keys():
    j = m-i
    if sum2[j]:
        answer+=(sum1[i]*sum2[j])


print(answer)