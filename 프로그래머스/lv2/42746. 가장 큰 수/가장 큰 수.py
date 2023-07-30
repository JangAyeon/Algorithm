# 테스트 11 : [0,0,0] -> 0

def solution(numbers):
    arr = list(map(str, numbers))
    
    arr.sort(reverse= True, 
            key=lambda x : (x*3))
    answer = str(int("".join(arr)))

    return answer