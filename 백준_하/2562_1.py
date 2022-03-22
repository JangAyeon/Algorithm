# 문제 : https://www.acmicpc.net/problem/2562

import sys

N = 9
# 문자열 n줄을 입력받아 리스트에 저장할 때
arr = [int(sys.stdin.readline().strip()) for i in range(N)]
ans = 0
for i in range(len(arr)):
    if ans < arr[i]:
        ans = arr[i]
        ans_idx = i+1


print(ans)
print(ans_idx)
