import sys
input = sys.stdin.readline
from collections import deque

n, m = map(int, input().split())
dDeck, sDeck = deque(), deque()
dGround, sGround = deque(), deque()

for _ in range(n):
    a, b= map(int, input().split())
    dDeck.appendleft(a)
    sDeck.appendleft(b)
    

# 도도 차례
check = True

while True:
    if check:
        dCard = dDeck.popleft()
        dGround.appendleft(dCard)
        check = False
        
    else:
        sCard = sDeck.popleft()
        sGround.appendleft(sCard)
        check = True
        
    ## 덱이 비어잇는 경우 게임 종료
    if not dDeck or not sDeck:
        break
    
    ## 도도가 이김
    ## 가장 위에 위치한 카드의 숫자가 5가 나오는 순간
    if (not check and dCard==5) or (check and sCard==5):
        # 상대방의 그라운드에 있는 카드 더미를 뒤집어 (마지막 꺼부터 나와야함)
        # 자신의 덱 아래로 그대로 합친 후 (마지막에 추가해야함)
        while sGround:
            dDeck.append(sGround.pop())
            
        # 자신의 그라운드에 있는 카드 더미 역시 뒤집어 
        # 자신의 덱 아래로 그대로 가져와 합침
        while dGround:
            dDeck.append(dGround.pop())
            
    
            
        
    ## 수연이가 이김
    ## 가장 위에 위치한 카드의 숫자 합이 5가 되는 순간
    ## 어느 쪽의 그라운드도 비어있으면 안된다
    if sGround and dGround and (sGround[0]+dGround[0])==5:
        while dGround:
            sDeck.append(dGround.pop())
        while sGround:
            sDeck.append(sGround.pop())
    # 차례 한 번 지남
    m-=1
    if m == 0:
        break
        
        
s, d = len(sDeck), len(dDeck)
if s==d:
    print("dosu")
elif s<d:
    print("do")
else:
    print("su")
        
        