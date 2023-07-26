def check(answer):
    for x,y,a in answer:
        if a == 0: # 기둥
            # 바닥 위에 
            if y ==0 :
                continue
            # 보의 한쪽 끝 부분 위에
            elif [x-1, y, 1] in answer or [x,y,1] in answer:
                continue
            # 다른 기둥 위에 
            elif [x, y-1, 0] in answer:
                continue
            else:
                return False
        else: # 보
            # 한쪽 끝 부분이 기둥 위에
            if [x, y-1, 0] in answer or [x+1, y-1, 0] in answer:
                continue
            # 양쪽 끝 부분이 다른 보와 동시에 연결되어
            elif [x-1, y, 1] in answer and  [x+1, y, 1] in answer:
                continue
            else:
                return False
            
    return True


def solution(n, build_frame):
    answer = []
    
    for x,y,a,b in build_frame:
        if b == 0: # 삭제
            answer.remove([x,y,a])
            if not(check(answer)): # 건물 불가능한 경우
                answer.append([x,y,a])
        else: # 설치
            answer.append([x,y,a])
            if not(check(answer)): # 건물 불가능한 경우
                answer.remove([x,y,a])
    answer.sort()
    return answer
    
    