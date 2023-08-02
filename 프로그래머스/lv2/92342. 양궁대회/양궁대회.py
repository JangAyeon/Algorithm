
def cal_score(rinfo, ainfo):
    rscore = 0
    ascore = 0
    for idx in range(len(rinfo)):
        if rinfo[idx] == ainfo[idx] == 0:
            continue
        elif rinfo[idx]>ainfo[idx]:
            rscore+=(10-idx)
        else:
            ascore+=(10-idx)
        
    return rscore - ascore

def better(info2, info1):
    r_info2 = list(reversed(info2))
    r_info1 = list(reversed(info1))
    for idx in range(len(r_info2)):
        if r_info2[idx]>r_info1[idx]:
            return True
        elif r_info1[idx]>r_info2[idx]:
            return False
    return False

def search(idx, n, rinfo, ainfo):
    if idx==11 or n == 0:
        rinfo[-1] = n
        diff = cal_score(rinfo, ainfo)
        return diff, rinfo[:]
    
    # 안 쏘고 넘기는 경우
    diff1, info1 = search(idx+1, n, rinfo, ainfo)
    
    # 화살 쏘는 경우 (복구 해야함)
    if n > ainfo[idx]:
        rinfo[idx] = ainfo[idx]+1
        diff2, info2 = search(idx+1, n - rinfo[idx], rinfo, ainfo)
        rinfo[idx] = 0
        if (diff2>diff1) or ((diff2 == diff1) and (better(info2, info1))):
            return diff2, info2
            
    return diff1, info1
    


def solution(n, info):
    diff, answer = search(0, n, [0]*11, info)
    if diff<=0:
        return [-1]
    return answer

