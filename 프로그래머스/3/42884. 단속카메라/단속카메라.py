

def solution(routes):
    answer = 1
    routes.sort()
    start,end =routes[0]

    for s,e in routes: ## 구간을 좁히고 ## 그 좁은 구간 안에 속하지 못하면 갱신
        if start<=s<=end:
            start = max(start, s)
            end = min(end, e)
        else:
            start = s
            end = e
            answer+=1
        ##print(s,e,start,end,answer)

    return answer