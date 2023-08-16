import sys
from collections import deque
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    n,m =map(int, input().split())
    que = deque(map(int, input().split()))
    idx = deque(range(0,n))
    answer=0
    
    while True:
        
        # 대기열 가장 앞에 있는 것 = 가장 중요도 높은것
        if que[0]==max(que):
            answer +=1
            
            # 동일한 중요도이면서 찾던 문서 번호임
            if idx[0]==m:
                print(answer)
                break
            else:
                que.popleft()
                idx.popleft()
        
        # 대기열 가장 앞에 있는것 != 가장 중요도 높은 것
        # 대기열 뒤로 넘기기
        else:
            que.append(que.popleft())
            idx.append(idx.popleft())