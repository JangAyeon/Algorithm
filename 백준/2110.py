import sys
input = sys.stdin.readline

n, c = map(int, input().split())
house = sorted([int(input().strip()) for _ in range(n)])

def get_count(dist, house):
    count=1
    pos = house[0]

    for next in house:
        if next - pos >= dist: # 이전 공유기와 지금 공유기의 거리가 제시된 거리 넘는 경우 설치
            pos = next
            count+=1
    return count


def get_bound(left, right, limit, house):
    
    while left <= right:
        mid = (left + right)//2
        count = get_count(mid, house)

        if count>=limit:
            # 라우터 갯수 많음 = 거리 너무 좁다는 소리 => 거리를 늘려야 함
            left = mid +1
        else:
            # 라우터 갯수 적음 = 거리 너무 넓다는 소리 => 거리를 좁혀야 함
            right = mid -1
    return left




print(get_bound(1, house[-1]-house[0], c, house)-1)
