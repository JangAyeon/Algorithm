from collections import defaultdict

def solution(weights):
    answer = 0
    ws = defaultdict(int)
    
    for w in weights:
        ws[w]+=1
    
    keys = list(ws.keys())
    for idx1 in range(len(keys)):
        for idx2 in range(idx1, len(keys)):
            w1, w2 = keys[idx1], keys[idx2]
            if w1==w2 and ws[w1]>1:
                answer+=((ws[w1])*(ws[w1]-1)//2)
            elif w1/w2 in [2/3, 2/4, 3/4, 3/2, 4/2, 4/3]:
                answer+=ws[w1]*ws[w2]
        


    return answer