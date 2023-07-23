import sys
input = sys.stdin.readline


def solution(x):
    if x == N:
        global result
        result+=1
        return
    for y in range(N):
        if array1[y] or array2[x+y] or array3[x-y+N-1]:
            continue
        array1[y] = array2[x+y] = array3[x-y+N-1] = True
        solution(x+1)
        array1[y] = array2[x+y] = array3[x-y+N-1] = False

N = int(input().strip())
array1 = [False]*N
array2 = [False]*(2*N-1)
array3 = [False]*(2*N-1)
result = 0
solution(0)
print(result)
