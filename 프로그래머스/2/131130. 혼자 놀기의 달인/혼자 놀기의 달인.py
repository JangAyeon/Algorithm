def solution(cards):
    cards = [i-1 for i in cards]
    n = len(cards)
    ##print(cards)
    visited = [False]*(n)
    counts = []
    for idx in range(n):
        count=0
        while not(visited[idx]):
            visited[idx]=True
            idx=cards[idx]
            ##print(idx, visited, cards[idx])
            count+=1
        counts.append(count)
    counts.sort(reverse=True)
    answer=counts[0]*counts[1]
    return answer