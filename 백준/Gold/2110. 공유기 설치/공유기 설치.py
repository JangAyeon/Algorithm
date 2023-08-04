import sys
input = sys.stdin.readline

n, c =map(int, input().split())
house = sorted([int(input()) for _ in range(n)])


def count_router(dist, house):
    # 첫번째 집에는 무조건 공유기 설치
    count = 1
    pos = house[0]

    for next_pos in house:
        if next_pos - pos >= dist: # 거리가 dist 넘는 경우 공유기 설치
            count+=1
            pos = next_pos
    return count

def get_upper_bound(left, right, target, house):
    while left <= right:
        mid = (left + right)//2
        router = count_router(mid, house)

        if router >= target:
            left = mid + 1
        else:
            right = mid - 1
    return left



print(get_upper_bound(1, house[-1]-house[0], c, house) - 1)
