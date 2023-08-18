def solution(N, stages):

    peoples = len(stages)
    stages.sort()
    fail = [ 0 for _ in range(N+1)]
    for idx in stages:
        if idx==N+1:
            continue
        fail[idx]+=1
    stage_rate = []
    fail = fail[1:]
    for idx, count in enumerate(fail):
        fail_players = fail[idx]
        stage_players = peoples-sum(fail[:idx])
        if stage_players == 0:
            rate = 0
        else:
            rate = fail_players/stage_players
        stage_rate.append([rate, idx+1])
    stage_rate.sort(key=lambda x : (-x[0] ))
    answer = []
    for rate, num in stage_rate:
        answer.append(num)
    return answer