def solution(brown, yellow):
    answer = []
    a = (brown-4)/2
    for x in range(50001):
        y = a-x
        if(x*y == yellow):
            break
    answer = [int(y+2), int(x+2)]
    return answer