# https://school.programmers.co.kr/learn/courses/30/lessons/12902
# 시간 초과

def solution(n):
    
#6, 41
#8, 153
#10, 571
#12, 2131
#14, 7953
    
    temp = [[0,2] for _ in range(n+1)]
    temp[2]=[0,3]
    
    for idx in range(4,len(temp),2):
        #print("##",idx)
        ans = []
        for i in range(2, idx+2,2):
            a = sum(temp[i])
            b = temp[idx-i][-1]
            #print(i,",",idx-i,":",a,b)
            if idx-i == 0:
                ans.append(2)
            else:
                ans.append(a*b)
        temp[idx]=ans
        
    #print(temp[-1])
    answer = sum(temp[-1])%1000000007
    return answer
    


            
            
            
        
        