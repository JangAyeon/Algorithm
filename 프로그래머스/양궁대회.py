from copy import deepcopy

answer = []
max_diff = 0


def cal_diff(info, myshot):
    apeach, my = 0, 0
    for i in range(11):
        if (info[i], myshot[i]) == (0, 0):
            continue
        if info[i] >= myshot[i]:
            apeach += (10 - i)
        else:
            my += (10 - i)
    return my - apeach

def dfs(info, myshot, n, i):
    global answer, max_diff
    if i == 11:
        if n!=0:
            myshot[10] = n
        score_diff = cal_diff(info, myshot)
        #print(score_diff)
        if score_diff <=0:
            return 
        result = deepcopy(myshot)
        
        if score_diff > max_diff:
            max_diff = score_diff
            answer = [result]
            return
        if score_diff == max_diff:
            answer.append(result)
            #print(answer)
        return
    
    # 점수 먹는 경우
    if info[i] < n:
        myshot.append(info[i] + 1)
        dfs(info, myshot, n - info[i] - 1, i + 1)
        myshot.pop()
    
    # 점수 안먹는 경우
    myshot.append(0)
    dfs(info, myshot, n, i + 1)
    myshot.pop()


    #print(info, myshot, n, i)

def solution(n, info):
    global max_diff, answer
    dfs(info, [], n, 0)
    if answer == []:
        return [-1]
    answer.sort(key = lambda x : x[::-1], reverse=True)
    return answer[0]
    


tests = [
    [5, [2,1,1,1,0,0,0,0,0,0,0]],
    [1, [1,0,0,0,0,0,0,0,0,0,0]],
    [9, [0,0,1,2,0,1,1,1,1,1,1]],
    [10, [0,0,0,0,0,0,0,0,3,4,3]]
]


for n, info in tests:
    print(solution(n, info))