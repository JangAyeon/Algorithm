def solution(citations):
    answer = 0
    for c in range(1,max(citations)+1):
        score = 0
        for i in citations:
            if i>=c:
                score+=1
        if c<=(score):
            answer =  c

    return answer