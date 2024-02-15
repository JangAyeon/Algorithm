from collections import deque
import sys
input = sys.stdin.readline

n = int(input())
# 카드 놓을 때 사용했던 기술을 뒤부터 이용해 정렬함
arr = reversed(list(map(int, input().split())))
res = deque(range(1,n+1))
que = deque()

for i in arr:
    p = res.popleft() 
    if i == 1:
        que.appendleft(p) # 리스트 맨 앞(0번째)에 추가
    elif i==2:
        que.insert(1,p) # 리스트 두번째 (1번째)에 추가
    else:
        que.append(p) # 가장 마지막에 추가



print(*que)