def solution(sizes):
    n = len(sizes)
    w = 0
    h = 0
    for idx in range(n):
        a,b = sizes[idx]
        if(a>b):
            sizes[idx]=[a,b]
        else:
            sizes[idx]=[b,a]
        w = max(w, sizes[idx][0])
        h = max(h, sizes[idx][1])
        ## print(w,h)

    answer = w*h
    return answer