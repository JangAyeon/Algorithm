## 백준 공유기 설치

import sys
input = sys.stdin.readline

n, c = map(int, input().split())
house = sorted([int(input().strip()) for _ in range(n)])

def get_count(dist, house):
    count=1
    pos = house[0]

    for next in house:
        if next - pos >= dist: # 이전 공유기와 지금 공유기의 거리가 제시된 거리 넘는 경우 설치
            pos = next
            count+=1
    return count


def get_bound(left, right, limit, house):
    
    while left <= right:
        mid = (left + right)//2
        count = get_count(mid, house)

        if count>=limit:
            # 라우터 갯수 많음 = 거리 너무 좁다는 소리 => 거리를 늘려야 함
            left = mid +1
        else:
            # 라우터 갯수 적음 = 거리 너무 넓다는 소리 => 거리를 좁혀야 함
            right = mid -1
    return left




print(get_bound(1, house[-1]-house[0], c, house)-1)


# 프로그래머스 기둥과 보
def check(answer):
    for x, y, a in answer:
        if a == 0: # 기둥
            if y==0:# 바닥 위
                continue
            elif [x-1, y, 1] in answer or [x,y,1] in answer: # 보의 한쪽 끝 부분 위
                continue
            elif [x, y-1, 0] in answer: # 다른 기둥 위에
                continue
            else:
                return False
        elif a == 1: # 보
            if [x, y-1, 0] in  answer or [x+1, y-1, 0] in answer: # 한쪽 끝 부분이 기둥 위
                continue
            elif [x-1, y, 1] in answer and [x+1, y, 1] in answer: # 양쪽 끝 부분이 다른 보와 동시에 연결
                continue
            else:
                return False
    return True


def solution(n, build_frame):
    answer = []
    for x, y, a, b in build_frame:
        if b == 0: # 삭제
            answer.remove([x,y,a])
            if not check(answer): # 삭제 못하는 경우
                answer.append([x,y,a])
        elif b == 1: # 설치
            answer.append([x,y,a])
            if not check(answer): # 설치 못하는 경우
                answer.remove([x,y,a])
    answer.sort()
    print(answer)
    return answer