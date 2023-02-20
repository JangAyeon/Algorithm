# 문제 : https://www.acmicpc.net/problem/1941
# 재귀 알고리즘으로 조합 구하기 : https://www.youtube.com/watch?v=q0s6m7AiM7o

import sys
input=sys.stdin.readline
from collections import deque

arr = [input().strip() for _ in range(5)]
#print(arr)
count = 0
dx=[1,-1,0,0]
dy=[0,0,1,-1]


def checkS(group): # 이다솜파 적어도 4명
    s_cnt = 0
    for x,y in group:
        if arr[x][y]=="S":
            s_cnt+=1
    return False if s_cnt<4 else True

def checkAdj(group): # 서로 가로 또는 세로로 인접
    visited=[False]*7 # 방문 여부
    que = deque()
    que.append(group[0])
    visited[0]=True

    while que:
        x,y=que.popleft()
        for i in range(4): #가로 세로 탐사
            nx = x + dx[i]
            ny = y + dy[i]
            if (nx,ny) in group: # 해당 좌표가 조합 내 있음 
                idx = group.index((nx,ny))
                if not visited[idx]: # 아직 방문 전임
                    visited[idx]=True
                    que.append((nx,ny))

    return False if False in visited else True



def solution(level, start, group):
    global count
    if level==7: # 조합 완성됨
        if checkAdj(group) and checkS(group): #조건 만족하는 경우 갯수 증가
            count+=1
        return
    for i in range(start, 25): #조합 만들기 - 재귀 이용
        solution(level+1, i+1, group+[divmod(i,5)])


solution(0,0,[])
print(count)