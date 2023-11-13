import sys
input = sys.stdin.readline

L,C = map(int, input().split())
arr = sorted(list(input().split()))
#print(L,C,arr)

def solution(len, idx, c_cnt, v_cnt, text):
    if len == L:
        if v_cnt>=1 and c_cnt>=2:
            print(text)
        return
    for i in range(idx, C):
        if arr[i] in ('a', 'e', 'i', 'o', 'u'):
            solution(len+1, i+1, c_cnt, v_cnt+1, text+arr[i])
        else:
            solution(len+1, i+1, c_cnt+1, v_cnt, text+arr[i])



solution(0, 0, 0, 0, "")


