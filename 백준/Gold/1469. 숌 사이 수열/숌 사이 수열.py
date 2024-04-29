import sys
input = sys.stdin.readline

def dfs(count, N, S, X):
    if count == N:
        print(*S)
        exit()
    
    for i in X:
        if i in S:
            continue
        next_idx = S.index(BLANK)
        if next_idx + i + 1 >= N * 2:
            break
        if S[next_idx + i + 1] != BLANK:
            continue

        S[next_idx] = i
        S[next_idx + i + 1] = i
        dfs(count+1, N, S, X)
        S[next_idx] = BLANK
        S[next_idx + i + 1] = BLANK

BLANK = -1
N = int(input())
X = sorted(list(map(int, input().split())))
S = [BLANK] * (N * 2)
dfs(0, N, S, X)
print(-1)



