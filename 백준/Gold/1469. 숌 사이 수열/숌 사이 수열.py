import sys
input = sys.stdin.readline

n = int(input())
arr = sorted(list(map(int, input().split())))
blank = -1

lst = [blank]*(2*n)


def dfs(depth, s):

    if depth==n:
        print(*s)
        exit()

    for x in arr:
        if x in s:
            continue
        idx = s.index(blank)
        if idx+x+1>=2*n:
            break
        if s[idx+x+1]!=blank:
            continue
        s[idx]=x
        s[idx+x+1]=x
        dfs(depth+1, s)
        s[idx]=blank
        s[idx+x+1]=blank

dfs(0, lst)
print(-1)