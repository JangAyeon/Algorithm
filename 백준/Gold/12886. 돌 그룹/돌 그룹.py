import sys
from collections import deque
input = sys.stdin.readline


[a,b,c] = list(map(int, input().split()))
total = a+b+c
visited = [[False for _ in range(total)] for _ in range(total)]


if total%3!=0:
    print(0)
    exit()


def bfs(n1,n2):
    que= deque()
    que.append([n1,n2])
    visited[n1][n2]=True
    while que:
        a,b = que.popleft()
        c = total-(a+b)
        if(a==b) & (b==c):
            print(1)
            exit()
        for x,y in [[a,b], [a,c], [b,c]]:
            if x>y:
                x,y=y,x
            elif x==y:
                continue

            x,y = x+x, y-x
            min_ = min(x,y,total-(x+y))
            max_ = max(a,y, total-(x+y))
            if not(visited[min_][max_]):
                que.append([min_, max_])
                visited[min_][max_]=True

bfs(a,b)
print(0)
                
                