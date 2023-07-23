import sys
input = sys.stdin.readline

n, m = map(int, input().strip().split())
know = set(map(int, input().split()[1:]))
party = [set(map(int, input().split()[1:])) for _ in range(m)]



# 거짓말 여부 확인하고 매번 다시 파티 전체 iteration 돌게 함
for _ in range(m): 
    for  p  in party:
        print(p, know)
        if (p & know):
            know = know | p

answer  = 0
for p in party:
    if p & know:
        continue
    else:
        answer+=1

print(answer)