from itertools import permutations

def check(users, bans):
    
    for i in range(len(users)):
        # 단어 길이 비교
        if len(users[i])!=len(bans[i]):
            return False
        # 단어 내 철자 비교
        for idx in range(len(users[i])):
            if bans[i][idx]=="*":
                continue
            if users[i][idx]!=bans[i][idx]:
                return False
    return True


def solution(user_id, banned_id):
    user_permutation = list(permutations(user_id, len(banned_id)))
    # 응모자 아이디 부분 조합을 만들어 그게 불량 사용자랑 매핑되는지 확인
    answer = []
    for users in user_permutation:
        if check(users, banned_id):
            if set(users) not in answer:
                answer.append(set(users)) 
                # set으로 추가하지 않으면 (a, b, c)와 (b, c, a) 서로 다른 걸로 인식함
    return len(answer)