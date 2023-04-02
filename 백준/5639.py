import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

# 무한 입력
arr = []
while True:
    try:    
        arr.append(int(input().strip()))
    except:
        break

def solution(subList):

    if len(subList) == 0: # 트리 종결
        return
    
    tempL, tempR = [], []
    mid = subList[0] # 루트 노드

    flag = False # 루트 노드 기준 리스트를 왼/오 트리로 나눌 수 있는지 여부 판정
    for i in range(1, len(subList)):
        if subList[i]>mid:
            flag = True
            tempL = subList[1:i] # 루트 노트 빼야함
            tempR = subList[i:]
            break # 더이상 리스트에서 왼/오 트리 나눌 필요 없음

    if not flag: # 분할 없는 경우
        tempL=subList[1:] # tempR = []로 초기화 상태랑 동일 해서 그냥 안씀...

    ## 후위 순회 
    solution(tempL)
    solution(tempR)
    print(mid)

solution(arr)