import sys
input = sys.stdin.readline

n,m = map(int, input().split())
know = set(map(int, input().split()[1:]))
party = [set(map(int, input().split()[1:])) for _ in range(m)]
story = [1]*m # 1 : 과장된 이야기, 0 : 진실된 이야기

for _ in range(m):
    for idx, i in enumerate(party):
        if know & i:
            story[idx]=0
            know = know | i # 집합 추가
            #print(know)
        #print(idx, i)


print(sum(story))