def check(answer):
    for x,y,a in answer:
        if a == 0: # 기둥 확인
            # 바닥 위, 보 한 쪽 끝, 다른 기둥 위
            if y == 0 or [x-1, y, 1] in answer or [x, y , 1] in answer or [x, y-1, 0] in answer:
                continue
            return False
        elif a == 1: # 보 확인
            # 한쪽 끝이 기둥 위, 양쪽 끝이 보와 연결
            if [x, y-1, 0] in answer or [x+1, y-1,0] in answer or ([x+1, y, 1] in answer and [x-1, y, 1] in answer):
                continue
            return False
        
    return True


def solution(n, build_frame):
    answer = []
    for x,y,a,b in build_frame:
        if b == 1: # 설치
            answer.append([x,y,a])
            if not check(answer):
                answer.remove([x,y,a])
        elif b == 0: # 삭제
            answer.remove([x,y,a])
            if not check(answer): 
                answer.append([x, y, a])
    answer.sort()
    #print(answer)
    return answer