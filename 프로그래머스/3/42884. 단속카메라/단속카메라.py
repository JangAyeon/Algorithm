def solution(routes):
    routes.sort()
    ##print(routes)
    start, end = routes[0]
    answer = 1
    for s, e in routes[1:]:
        if start<=s<=end:
            start = s
            end=min(end,e)
        else:
            start=s
            end=e
            answer+=1
        ##print(start, end)

    return answer