def solution(N, stages):
    stages.sort()
    fails = []
    answer = []
    for step in range(1, N+1):
        count = 0
        n = len(stages)
        while (stages and stages[0]<=step):
            count+=1
            stages.pop(0)
        if (n):
            fails.append([count/n, step])
        else:
            fails.append([0, step])
        

    fails.sort(key=lambda x:(-x[0],x[1]))

    for f, s in fails:
        answer.append(s)
    return answer
