def solution(data, ext, val_ext, sort_by):

    sortKey={"code":0,"date":1, "maximum":2, "remain":3}
    answer = []
    for d in data:
        if d[sortKey[ext]]<val_ext:
            answer.append(d)
    answer.sort(key=lambda x:x[sortKey[sort_by]])
    ##print(answer)
            
    return answer