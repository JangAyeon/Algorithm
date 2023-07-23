import sys
input = sys.stdin.readline

n, m = map(int, input().strip().split())
know = set(map(int, input().split()[1:]))
party = [set(map(int, input().split()[1:])) for _ in range(m)]




for _ in range(m):
    for  p  in party:
        if (p & know):
            know = know | p

answer  = 0
for p in party:
    if p & know:
        continue
    else:
        answer+=1

print(answer)