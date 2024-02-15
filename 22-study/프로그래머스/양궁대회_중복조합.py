from itertools import combinations_with_replacement


def cal_diff(apeach, lyan):
    apeach_score, lyan_score = 0, 0
    for i in range(11):
        if apeach[i] == lyan[i] == 0:  # 라이언과 어피치 모두 한번도 화살을 맞히지 못한 경우
            continue
        elif apeach[i] >= lyan[i]:  # 어피치가 라이언이 쏜 화살의 수 이상을 맞힌 경우
            apeach_score += 10 - i
        else:  # 라이언이 어피치보다 많은 수의 화살을 맞힌 경우
            lyan_score += 10 - i

    return lyan_score - apeach_score

def solution(n, apeach):
    answer = [-1]
    max_gap = -1  # 점수 차

    for combi in combinations_with_replacement(range(11), n):  # 중복 조합으로 0~10점까지 n개 뽑기
        lyan = [0] * 11  # 라이언의 과녁 점수

        for i in combi:  # combi에 해당하는 화살들을 라이언 과녁 점수에 넣기
            lyan[10 - i] += 1

        gap = cal_diff(apeach, lyan)

        if gap>max_gap and gap>0:  # 라이언이 점수가 더 높은 경우
            max_gap = gap
            answer = lyan
    return answer

tests = [
    [5, [2,1,1,1,0,0,0,0,0,0,0]],
    [1, [1,0,0,0,0,0,0,0,0,0,0]],
    [9, [0,0,1,2,0,1,1,1,1,1,1]],
    [10, [0,0,0,0,0,0,0,0,3,4,3]]
]


for n, info in tests:
    print(solution(n, info))