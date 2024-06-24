## n 길이로 받을 수 있는 인원수가 m보다 작음
# -> n 길이 줄이기

## 주어진 길이로 몇 개 과자 나오는지 (몫을)

## M명의 조카,  N개의 과자

import sys
input = sys.stdin.readline

def get_count(lst, length):
    count=0
    for slice in lst:
        count+=(slice//length)

    return count




m,n = map(int, input().split())
lst = list(map(int, input().split()))
lst.sort()

left = 1
right = lst[-1]


answer = 0
while left<=right:
    mid = (left+right)//2
    count = get_count(lst, mid)
    if count<m:
        right = mid-1
        
    else:

        answer = max(answer, mid)

        left=mid+1
print(answer)
    