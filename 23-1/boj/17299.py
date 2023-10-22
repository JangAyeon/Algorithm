from collections import Counter
import sys
input = sys.stdin.readline


n = int(input())
arr = list(map(int, input().split()))
cnt = Counter(arr) # 숫자 빈도수 
res = [-1]*n
stack = [0]


for i in range(1,n):
    # 현재 숫자가 스택 가장 위 값 인덱스로 입력 받은 배열에 있는 숫자보다 빈도수가 높으면 추가
    while stack and cnt[arr[stack[-1]]]<cnt[arr[i]]:
        res[stack.pop()]=arr[i]

    stack.append(i)


print(*res)