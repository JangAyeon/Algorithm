from collections import Counter

def solution(X, Y):
    X, Y= list(X),list(Y)
    x1,x2 = set(X),set(Y)
    numbers = x1.intersection(x2)
    cntX, cntY = Counter(X), Counter(Y)
    ##print(numbers,X,Y)
    lst = []
    if not(numbers):
        return "-1"
    elif numbers=={"0"}:
        return "0"
    else:
        for x in numbers:
            count = min(cntX[x],cntY[x])
            for _ in range(count):
                lst.append(x)
        lst.sort(reverse=True)
        answer = "".join(lst)
        return answer
