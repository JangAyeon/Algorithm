import sys
input = sys.stdin.readline

n = int(input())
arr1 = list(map(int, input().split()))
arr2 = list(map(int, input().split()))
answer = 0

while(arr1):
    a = min(arr1) 
    b = max(arr2)
    answer += a*b
    arr1.remove(a)
    arr2.remove(b)
    
print(answer)