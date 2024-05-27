def solution(citations):
    answer = 0
    citations.sort(reverse=True)
    print(citations)
    for num, citation in enumerate(citations, start=1):
        # 피 인용수가 논문의 수랑 같아지는 지점(num은 1부터 시작하도록)
        if citation >= num: 
            answer = h_index = num

    return answer