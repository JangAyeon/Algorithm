def solution(routes):
    answer = 1
    routes.sort()
    start, end = routes[0]
    for s,e in routes:
        if(start<=s <=end):
            start = max(start, s)
            end = min(end, e)
        else:
            answer+=1
            start = s
            end =e
        print(s,e, start, end, answer)
    print(routes)
    return answer