# 라이언 점수표, 어피치 점수표 
def cal_score(rinfo, ainfo):
    r_score = a_score = 0
    for i in range(len(rinfo)):
        if ainfo[i]==rinfo[i]==0:
            continue
        elif ainfo[i]>=rinfo[i]:
            a_score+=(10-i)
        else:
            r_score+=(10-i)
    return r_score - a_score

# 작은 점수 순으로 확인해서 더 적게 쏜 순간 False
def better(info2, info1):
    r_info2 = list(reversed(info2))
    r_info1 = list(reversed(info1))
    for idx in range(len(info2)):
        if r_info1[idx]>r_info2[idx]:
            return False
        elif r_info2[idx]>r_info1[idx]:
            return True
            
    return False
    

# 현재 탐색 점수 인덱스, 남은 화살수, 라이언 화살표, 어피치 화살표
def search(idx, n, rinfo, ainfo):
    if idx == 11 or n==0:
        rinfo[-1]=n
        diff = cal_score(rinfo, ainfo)
        return diff, rinfo[:]
    # 안쏘고 넘어가는 경우
    diff1,info1 = search(idx+1, n, rinfo, ainfo)
    
    # 쏘고 넘어가는 경우 
    if n>ainfo[idx]:
        rinfo[idx] = ainfo[idx]+1
        diff2, info2 = search(idx+1, n -rinfo[idx], rinfo, ainfo)
        rinfo[idx] = 0
        if diff2>diff1 or ((diff2 == diff1) and (better(info2, info1))):
            return diff2, info2
    return diff1, info1


def solution(n, info):
    diff, answer = search(0, n,[0]*11,info)
    if diff<=0: return [-1]
    return answer

