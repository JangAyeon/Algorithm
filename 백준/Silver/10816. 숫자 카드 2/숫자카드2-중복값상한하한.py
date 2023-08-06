import sys
input = sys.stdin.readline

n = int(input())
card = sorted(list(map(int, input().split())))
m = int(input())
find = list(map(int, input().split()))
answer = []


def binary_search(card, target, start, end):
    
    # 전체에서 target 찾지 못한 경우
    if start>end:
        return 0
    
    mid = (start+end)//2
    
    if card[mid] == target:
        #print("find", mid, target)
        i = j = 1
        # lower bound 추적 
        # 최대 start 지점까지만 내려가 탐색.. 그 이전은 target 아님이 판명됨
        while start<=mid-i and card[mid-i]==target:
            #print("lower",mid-i)
            i+=1
        # upper bound 추적
        # 최대 end 지점까지만 올라가 탐색... 그 이후는 target 아님이 판명됨
        while mid+j<=end and card[mid+j]==target:
            #print("upper", mid+j)
            j+=1
        return i+j-1
            
    elif card[mid]>target:
        end = mid-1
        return binary_search(card, target, start, end) # return을 해야 count를 받음
    elif card[mid]<target:
        start = mid+1
        return binary_search(card, target, start, end) # return을 해야 count를 받음
    
count_dic = {}
for target in find:
    start = 0
    end = len(card)-1
    
    # 이전에 갯수 구한 target에 대해 또 갯수 구하는 거 방지
    if target not in count_dic:
        count_dic[target] = binary_search(card, target, start, end)
        
print( " ".join(str(count_dic[target]) for target in find))
