# https://school.programmers.co.kr/learn/courses/15008/lessons/121684

answer = 0

def transpose(ability):
    trans = [[0 for _ in range(len(ability))] for _ in range(len(ability[0]))]
    for r in range(len(ability)):
        for c in range(len(ability[0])):
            trans[c][r] = ability[r][c]
            
    return trans

def DFS(L, s, ability, check):
    global answer
    n = len(ability[0])  # 학생 수
    m = len(ability)     # 종목 개수
    
    if L == m:
        answer = max(answer, s)   # 능력치 합의 최댓값을 구함
    else:
        for i in range(n):
            if not check[i]:
                check[i] = True
                DFS(L+1, s + ability[L][i], ability, check)
                check[i] = False


def solution(ability):
    global answer
    ability = transpose(ability)
    #print(trans)
    check = [False]*len(ability[0])
    print(check)
    DFS(0, 0, ability, check)      
    # L, sum, ability, check
    # L : 선택한 종목 갯수, sum : 능력치의 합, check : 선택되는 학생 배열
    
    return answerㄴ