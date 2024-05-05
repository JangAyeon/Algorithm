import sys

# 입력 받기
input_lines = sys.stdin.readlines()
l, w, h = map(int, input_lines[0].split())
totalV = l * w * h
n = int(input_lines[1])
arr = []

# 큐브 정보 입력 및 처리
for line in input_lines[2: n+2]:
    a, b = map(int, line.split())
    s = 2 ** a
    ## 부피, 갯수, 한변
    arr.append([s * s * s, b, s])

arr.sort(reverse=True, key=lambda x: x[0])

answer = 0
total_now = 0

# 큐브 채우기
for size, count, s in arr:
    ## # 다음 순서 = 이전 정육면체 부피의 1/8이므로 이전까지의 개수에 8을 곱해줌 (예 : 4*4*4 1개 = 2*2*2 8개)
    total_now *= 8
    cnt_limit = (l //s) * (h // s) * (w // s) - total_now
    cnt_limit = min(count, cnt_limit)
    answer += cnt_limit
    total_now += cnt_limit

if total_now != totalV:
    print(-1)
else:
    print(answer)
