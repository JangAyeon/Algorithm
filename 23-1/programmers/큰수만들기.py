# https://school.programmers.co.kr/learn/courses/30/lessons/42883

def solution(number, k):
    arr = []
    for i in number:
        if len(arr) == 0:
            arr.append(i)
            continue
        if k>0:
            while arr[-1]<i:
                arr.pop()
                k-=1
                if len(arr)==0 or k<1:
                    break
        arr.append(i)
    #print("".join(arr))
    arr  = arr[:-k] if k>0 else arr
    return "".join(arr)