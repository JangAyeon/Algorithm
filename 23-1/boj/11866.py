import sys
from collections import deque

n,k = map(int, input().split())
# 양방향 연결리스트 
que = deque([i for i in range(1, n+1)])

res = []
while que:
    for _ in range(k-1):
        # k-1번째 노드까지 맨 뒤로 ..
        que.append(que.popleft())
    # k번째 삭제 -> 결과에 추가
    res.append(str(que.popleft()))

print("<"+", ".join(res)+">")