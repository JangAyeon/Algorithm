import sys
input = sys.stdin.readline

N = int(input())
array = []

for _ in range(N):
    str = input().split() # split 한 상태로 바로 추가 X : 점수만 따로 숫자 처리해야 함 
    array.append([str[0], int(str[1]),int(str[2]), int(str[3])])


array.sort(key = lambda x : (-x[1],x[2],-x[3],x[0]))

for a in array:
    print(a[0])

