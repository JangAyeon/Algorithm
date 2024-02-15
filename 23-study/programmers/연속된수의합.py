def solution(num, total):
    answer = []
    if num%2==0: # 짝수인 경우
        bound = num//2
        x = 1/2*(total/bound+1)
        for i in range(-bound, bound):
            answer.append(x+i)
        
        
        
    else: # 홀수인 경우
        bound = num//2
        x = total//num
        for i in range(-bound, bound+1):
            answer.append(i+x)
    #print(answer, bound)
    return answer