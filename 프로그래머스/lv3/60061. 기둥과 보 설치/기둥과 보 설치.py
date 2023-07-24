
def isAble(answer):
    for x,y,a in answer:
        if a == 0: # 기둥
            # 바닥 위에 있거나 
            if y == 0: continue
            # 보의 한쪽 끝 부분 위에 있거나,
            elif [x-1, y, 1] in answer or [x,y,1] in answer: continue
            # 또는 다른 기둥 위에 있어
            elif [x,y-1 ,0] in answer: continue
            else: return False
             
        elif a == 1: # 보
            # 한쪽 끝 부분이 기둥 위에 있거나, 
            if [x,y-1,0] in answer or [x+1, y-1, 0] in answer: continue
            # 또는 양쪽 끝 부분이 다른 보와 동시에 연결
            elif  [x-1,y,1] in answer and [x+1,y,1] in answer: continue
            else: return False
    return True


def solution(n, build_frame):
    answer = []
    for x, y, a, b in build_frame:
        if b == 1: # 설치
            answer.append([x,y,a])
            if not(isAble(answer)): # 설치 불가능한 경우
                answer.remove([x,y,a])
        elif b == 0: # 삭제 
            answer.remove([x,y,a]) 
            if not(isAble(answer)): # 삭제 불가능한 경우
                answer.append([x,y,a])
    answer.sort()
    return answer