from collections import defaultdict

def solution(clothes):
    answer = 0
    clothDic = defaultdict(list)
    for v,k in clothes:
        clothDic[k].append(v)
    print(clothDic)
    total = 1
    for k in clothDic.keys():
        total*=(len(clothDic[k])+1)
    print(total)
    total-=1
    return total