import sys
input = sys.stdin.readline

n= int(input())
arr = sorted(list(map(int, input().split())))

def calc_distance(idx):
    loc = arr[idx]
    distance = 0
    for house in arr:
        distance+=abs(loc - house)
    return distance, loc

## 짝수인 경우
if len(arr)%2==0:
    answer = min(calc_distance(len(arr)//2), calc_distance(len(arr)//2-1))[1]

## 홀수인 경우  
else:
    answer = arr[len(arr)//2]
    
    
print(answer)

