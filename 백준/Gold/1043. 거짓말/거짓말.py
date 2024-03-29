import sys
input = sys.stdin.readline

n, m = map(int, input().strip().split())
know = set(map(int, input().split()[1:]))
party = [set(map(int, input().split()[1:])) for _ in range(m)]
lie = [1]*m


# 거짓말 여부 확인하고 매번 다시 파티 전체 iteration 돌게 함
for _ in range(m): 
    for idx, p  in enumerate(party):
        if (p & know):
            lie[idx] = 0
            know = know | p


print(sum(lie))