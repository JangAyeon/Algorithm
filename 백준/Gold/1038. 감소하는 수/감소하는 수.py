import sys

input= sys.stdin.readline
from collections import deque

n = int(input())
que = deque()
for i in range(10):
    que.append(str(i))

if n<10:
    print(que[n])
    exit()
else:
    count=9
    while que:
        i = que.popleft()
        for j in range(0, int(i[-1])):
            count+=1
            num = str(i)+str(j)
            if count==n:
                print(num)
                exit()
            else:
                que.append(str(i)+str(j))

print(-1)