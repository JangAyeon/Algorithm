
def solution(n, info):
    score_diff, answer = search(0, n, [0]*11, info)
    if score_diff <=0:
        return [-1]
    return answer
    
def calculate_score_diff(rinfo, ainfo):
    rscore = ascore = 0
    for idx in range(len(rinfo)):
        if rinfo[idx] == ainfo[idx] == 0:
            continue
        if rinfo[idx]>ainfo[idx]:
            rscore+=(10-idx)
        else:
            ascore+=(10-idx)
    return rscore - ascore

def better(info1, info2):
    r_info1 = list(reversed(info1))
    r_info2 = list(reversed(info2))
    for idx in range(len(info1)):
        if r_info1[idx]>r_info2[idx]:
            return True
        elif r_info1[idx]<r_info2[idx]:
            return False
    return False


def search(idx, n, rinfo, ainfo):
    if idx == 11 or n == 0:
        rinfo[-1] = n
        diff = calculate_score_diff(rinfo, ainfo)
        return diff, rinfo[:]
    
    diff1, rinfo1 = search(idx+1, n, rinfo, ainfo)
    if n > ainfo[idx]:
        rinfo[idx] = ainfo[idx]+1
        diff2, rinfo2 = search(idx+1, n - rinfo[idx], rinfo, ainfo)
        rinfo[idx] = 0
        if diff2 > diff1 or (diff2 == diff1 and better(rinfo2, rinfo1)):
            return diff2, rinfo2
    return diff1, rinfo1


