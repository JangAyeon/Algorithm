import sys
sys.setrecursionlimit(10**9)
input = sys.stdin.readline

arr = []
while True:
    try:
        arr.append(int(input()))
    except:
        break
    
    
def solution(subList):
    
    if len(subList)==0:
        return
    
    flag = False
    mid  = subList[0]
    
    for idx in range(1, len(subList)):
        if subList[idx]>mid:
            tempLeft = subList[1:idx]
            tempRight = subList[idx:]
            flag = True
            break
        
    if not(flag):
        tempLeft = subList[1:]
        tempRight = []
        
    solution(tempLeft)
    solution(tempRight)
    
    print(mid)
    
    
solution(arr)