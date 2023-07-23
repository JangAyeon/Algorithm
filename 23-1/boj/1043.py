import sys
input = sys.stdin.readline

n, m = map(int, input().strip().split())
tArray = set(map(int, input().strip().split()[1:]))
# 0 인 경우 tArray는 빈 리스트로 나옴 
party = []
answer = 0

for i in range(m):
    i = set(map(int,  input().strip().split()[1:]))
    party.append(i)
    for j in i:
        if j in tArray: # 진실 아는 사람 있음 
            tArray = tArray|i

for j in party:
    intersection  = j & tArray
    if not(intersection): answer+=1

print(answer)