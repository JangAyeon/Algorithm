def solution(n, lost, reserve):
    s_lost = set(lost) - set(reserve)
    s_reserve = set(reserve) - set(lost)
    
    for x in s_reserve:
        if x-1 in s_lost:
            s_lost.remove(x-1)
        elif x+1 in s_lost:
            s_lost.remove(x+1)
    
    answer = n - len(s_lost)
    return answer



