# 중복된 단어는 한번만 나오게
# 길이별로 묶기 -> 같은 길이 내에서 사전 순서 대로

N = int(input())
total_arr = [input() for _ in range(N)]
arr = set(total_arr)
M = 0
sort = {}

for i in arr:
    if len(i) not in sort.keys():
        sort[len(i)] = []

    sort[len(i)].append(i)
    if len(i) > M:
        M = len(i)

for i in range(1, M+1):
    if i in sort.keys():
        words = sorted(sort[i])
        for word in words:
            print(word)
