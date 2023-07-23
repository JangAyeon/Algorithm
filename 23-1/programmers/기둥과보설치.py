def isAble(answer):
    for x,y,t in answer:
        if t ==0: # 기둥
            #바닥 위에 있거나 
            if y == 0:
                continue
            #보의 한쪽 끝 부분 위에 있거나 - 이 조건 틀렸었음  
            elif [x-1,y,1] in answer or [x,y,1] in answer:
                continue
            #다른 기둥 위에 있어야 
            elif [x,y-1,0] in answer:
                continue
            else: # 그 어떠한 조건에도 속하지 않음 
                return False


        else: # 보

            # 한쪽 끝 부분이 기둥 위에 있음
            if ([x,y-1,0] in answer) or ([x+1,y-1,0] in answer):
                #print("한쪽 끌이 기둥 위에")
                continue
            # 양쪽 끝 부분이 다른 보와 동시에 연결
            elif (([x-1,y,1] in answer) and ([x+1,y,1] in answer)):
                #print("양쪽 끝이 다른 보와 동시에 연결")
                continue
            else:
                return False
        
    return True

def solution(n, build_frame):

    answer = []
    
    for x,y,t, build in build_frame:
        #print(x,y,t)
        if build == 1:# 삽입 
            answer.append([x,y,t])
            if not(isAble(answer)): # 설치 불가능한 경우
                answer.remove([x,y,t])
        else: # 삭제 
            answer.remove([x,y,t])
            if not(isAble(answer)): # 삭제 불가능한 경우 
                answer.append([x,y,t])

    answer.sort()
    return answer