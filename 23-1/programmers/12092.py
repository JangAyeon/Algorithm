# https://school.programmers.co.kr/learn/courses/30/lessons/12902
# 시간 초과

def solution(n):
    
#6, 41
#8, 153
#10, 571
#12, 2131
#14, 7953
    

    temp = [0 for _ in range(n+1)]
    temp[2]=3
    
    for idx in range(4, n+1,2):
        #print("idx: ",idx)
        ans = 0
        for i in range(2,idx+1,2):
            #print(i)
            if i+2 == idx:
                #print(i,"3배",3*temp[i],temp[i])
                ans+=3*temp[i]
            else:
                #print(i, "2배",2*temp[i])
                ans+=2*temp[i]
        temp[idx] = ans+2
        #print(temp)
    answer = temp[n]%1000000007
    return answer
    


            
            
            
        
        
            
            
            
        
        