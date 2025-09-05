from itertools import permutations

def solution(numbers):
    
    ## num = list(permutations(numbers.split("")))
    answer = []
    for i in range(1, len(numbers)+1):
        nums = set(list(map("".join,permutations(numbers, i))))
        arr = [int(j) for j in list(nums)]
       
        for j in arr:
            isPrime = True if j>1 else False
            for k in range(2, int(j**(1/2)+1)):
                if(j==k): continue
                if(j%k==0):
                    isPrime=False
                    break
            ## print(j, isPrime)
            if(isPrime):
                answer.append(j)
        ### 소수인지 여부 따져라
        
    
    ##print(answer)
    return len(list(set(answer)))