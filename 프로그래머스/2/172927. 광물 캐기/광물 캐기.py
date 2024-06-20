from collections import Counter

def solution(picks, minerals):
    answer = 0

    mineralSort = []

    for idx in range(0, min(sum(picks) * 5, len(minerals)),5):
        chunck = minerals[idx:idx+5]
        mineralSort.append([chunck.count("diamond"),chunck.count("iron"), chunck.count("stone")])
    mineralSort.sort(reverse=True)
    print(mineralSort)
    tool = 0
    for a,b,c in mineralSort:
        while picks[tool]==0:
            tool+=1
        if tool==0:
            answer+=(a+b+c)
        elif tool==1:
            answer+=(a*5+b+c)
        else:
            answer+=(25*a+5*b+c)
        picks[tool]-=1

    return answer