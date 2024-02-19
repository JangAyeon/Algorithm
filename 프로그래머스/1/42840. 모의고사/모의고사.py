def solution(answers):
    picks =[
    [1,2,3,4,5],
    [2, 1, 2, 3, 2, 4, 2, 5],
    [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]]
    corrects = []
    for pick in picks:
        correct = 0
        for idx in range(len(answers)):
            if (pick[idx%len(pick)]==answers[idx]):
                ## print(pick, idx%len(pick))
                correct+=1
        corrects.append(correct)
    max_v = max(corrects)
    answer = []
    for idx in range(len(corrects)):
        if (corrects[idx]==max_v):
            answer.append(idx+1)
            
    return answer