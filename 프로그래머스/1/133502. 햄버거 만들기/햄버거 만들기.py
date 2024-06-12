def solution(ingredient):
    answer = 0
    a, b = [], [] ## 재료, 빵
    n = len(ingredient)
    arr=[]
    for idx in range(n):
        arr.append(ingredient[idx])
        if ingredient[idx]==1:
            temp = []
            for _ in range(4):
                if arr:
                    temp.append(arr.pop())
            if temp==[1,3,2,1]:
                answer+=1
            else:
                while temp:
                    arr.append(temp.pop())
            

        
        
    return answer

