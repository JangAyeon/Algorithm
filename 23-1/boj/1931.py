import sys
input = sys.stdin.readline

n = int(input())
arr = [ list(map(int, input().split())) for _ in range(n)]

## 가장 일찍 끝나면서 가장 일찍 시작하는 순으로 정렬
# 회의 종료 시간의 오름 차순 정렬
# 같은 회의 종료 시간에 대해서 시작 시간이 이른 것 정렬
arr.sort(key = lambda x : (x[1], x[0]))

## 초기화
# 가장 일찍 끝나는 회의 선책
start = arr[0][0]
end = arr[0][1]
answer =1

## 탐욕적 선택
# 가장 먼저 끝나는 회의 순으로 선택
for s, e in arr[1:]:
    
    ## 실행 가능성
    # 현재 선택된 회의가 직전 회의 끝나고 시작되는 경우 추가 가능
    if end<=s:
        answer+=1
        end=e
        
print(answer)
        