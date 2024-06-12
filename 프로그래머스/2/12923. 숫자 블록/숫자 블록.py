def solution(begin, end):
    answer = [1]*(end-begin+1)
    n = len(answer)

    for i in range(n):
        k = i+begin
        for j in range(2,int(k**(1/2))+1):
            if k%j>0: ## 약수 아님
                continue
            temp = [answer[i],j]
            if k//j<= 10000000:
                temp.append(k//j)

            answer[i]= max(temp)

    if begin==1:
        answer[0]=0

    return answer