# https://school.programmers.co.kr/learn/courses/30/lessons/42883

def solution(number, k):
    arr = []
    for i in number:
        while len(arr)>0 and k>0 and arr[-1]<i:
            arr.pop()
            k-=1
        arr.append(i)
    arr = arr[:-k] if k>0 else arr
    return "".join(arr)