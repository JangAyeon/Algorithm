import sys
from collections import deque

input = sys.stdin.readline
N=int(input())
que = deque()
que.append([1,0,0])
visited = [[False] * (N+1) for _ in range(N+1)]

while(que):
    screen,clip, time = que.popleft()
    ## print(screen,clip, time)
    if(screen==N):
        print(time)  
        break
    ## 그냥 복사하기
    if(screen+clip<N+1 and visited[screen+clip][clip]==False):
        que.append([screen+clip,clip,time+1])
        visited[screen+clip][clip]=True
    ### 클립보드 바꾸기
    if(visited[screen][screen]==False):
        que.append([screen,screen,time+1])
        visited[screen][screen]=True

    ## 그냥 하나 삭제하기
    if(screen-1>0 and visited[screen-1][clip]==False):
        que.append([screen-1,clip,time+1])
        visited[screen-1][clip]=True


    

