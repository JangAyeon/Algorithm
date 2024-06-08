def solution(N, target):
    visited,dic = set(),dict()
    visited.add(0)
    for i in range(1,9):
        num = int(str(N)*i)
        if num ==target:
            return i
        dic[i]=[num]
        visited.add(num)

   
    for k in range(2,9):
        for i in range(1,k):
            j = k-i
   
            for a in dic[i]:
                for b in dic[j]:
           
             
                    numbers = [a+b,abs(a-b),a*b,a//b, b//a]
                    for num in numbers:
                        if num in visited:
                            continue
                        elif num==target:
                            return k
                        dic[k].append(num)
                        visited.add(num)
                 
    return -1