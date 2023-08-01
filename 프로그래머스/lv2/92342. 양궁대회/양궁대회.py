def solution(n, info):
    score_diff, answer = search(0, n, [0]*11, info)
    if score_diff<=0:
        return [-1]
    return answer
    
def cal_score(rinfo, ainfo):
    r_score = a_score = 0
    for i in range(len(rinfo)):
        if ainfo[i]==rinfo[i]==0:
            continue
        elif ainfo[i]>=rinfo[i]:
            a_score+=(10-i)
        else:
            r_score+=(10-i)
            
    return r_score-a_score
    
def better(info2, info1):
    r_info2 = list(reversed(info2))
    r_info1 = list(reversed(info1))
    
    for i in range(len(r_info2)):
        if r_info1[i]>r_info2[i]:return False
        
        elif r_info2[i]>r_info1[i]: return True
        
    return False
    
def search(idx, n, rinfo, ainfo):
    if idx==11 or n==0:
        rinfo[-1] = n
        diff = cal_score(rinfo, ainfo)
        return diff, rinfo[:]
    diff1, info1 = search(idx+1, n, rinfo, ainfo)
    if n > ainfo[idx]:
        rinfo[idx] = ainfo[idx]+1
        diff2, info2 = search(idx+1, n - rinfo[idx], rinfo, ainfo)
        rinfo[idx] = 0
        if ((diff2 == diff1) and better(info2, info1)) or diff2>diff1:
            return diff2, info2
    return diff1, info1
    
