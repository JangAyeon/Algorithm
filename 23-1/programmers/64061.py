# https://school.programmers.co.kr/learn/courses/30/lessons/64061

def solution(board, moves):
    
    answer = []
    count=0
    for i in moves:
        
        for j in range(len(board[i-1])):
            num = board[j][i-1]
            #print("##move##",i,num, answer,count)
            if num!=0:
                
                if len(answer)>0 and num==answer[-1]:
                    del answer[-1]
                    board[j][i-1] = 0
                    count+=2
                else:
                    board[j][i-1] = 0
                    answer.append(num)
                break
            else:
                continue
                    

    #print(count)
    return count