import sys
input =sys.stdin.readline

n, c = map(int,input().split())
house = sorted([int(input()) for _ in range(n)])


# 주어진 거리로 공유기 설치 갯수하는 함수
def install(distance, house):
    
    # 첫번째 집은 무조건 설치
    count=1
    curr_pos = house[0] #거리 측정 시작점
    
    for idx, next_pos in enumerate(house):
        curr_distance = next_pos - curr_pos
        if curr_distance>=distance:
            count+=1
            curr_pos = next_pos
            
    return count

        
    

# 거리 탐색하는 함수
def binary_distance(start, end, target, house):
    while start<=end:
        mid = (start+end)//2
        
        # mid 거리로 공유기 설치 갯수
        installed = install(mid,house)
        
        
        # 공유기 갯수가 많아서 줄여야함
        # 사이 간격 늘리기
        if installed>=target: 
            # 갯수가 목표한 갯수 start 지점을 최대한 뒤로 미뤄서 최소 거리를 구함
            start = mid+1
        else:
            end = mid-1
    return start - 1 # 예제에서 4-1(첫 집시작점) = 3으로 규정함
        

print(binary_distance(1, house[-1] - house[0],c, house))
