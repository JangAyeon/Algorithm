import sys
input = sys.stdin.readline
from collections import deque


arr = [deque(map(int, list(input().strip()))) for _ in range(4)] # ❤️ deque로 입력 받아야 나중에 회전 처리하기 쉬움
# N극은 0, S극은 1로 나타나있다.
k = int(input().strip())

cmd = []
for _ in range(k):
    idx, direction = map(int, input().split())
    cmd.append([idx-1, direction]) # ❤️ 0 - indexing 처리 (앞으로 반복문 처리 및 인덱싱을 위해)
# 첫 번째 정수는 회전시킨 톱니바퀴의 번호, 두 번째 정수는 방향이다. 방향이 1인 경우는 시계 방향이고, -1인 경우는 반시계 방향이다.

def checkLeft(idx, direction):
    if idx<0 or arr[idx][2]==arr[idx+1][6]: # 재귀 중지 조건
        return
    else:
        # 재귀적으로 바로 다음 왼쪽도 회전 가능한지
        checkLeft(idx-1, -direction)
        arr[idx].rotate(direction)
        #print("rotate Light Side")

def checkRight(idx, direction):
    if idx>3 or arr[idx-1][2]==arr[idx][6]: # 재귀 중지 조건 
        return
    else:
        # 바로 오른쪽도 회전 가능한지
        checkRight(idx+1, -direction)
        arr[idx].rotate(direction)
        #print("rotate Right Side")

def calScore():
    res = 0
    for i in range(4):
        #print("score", i, arr[i][0])
        if arr[i][0]==1:
            res+=pow(2,i)
    return res


def solution():
    for idx,direction in cmd:

        # 왼쪽 톱니 바퀴 회전 가능 여부 확인 및 회전
        checkLeft(idx-1, -direction)
        # 오른쪽 톱니 바퀴 회전 가능 여부 확인 및 회전
        checkRight(idx+1, -direction)
        # 기준 톱니 바퀴 회전
        arr[idx].rotate(direction)
    
    score = calScore()
    print(score)

solution()