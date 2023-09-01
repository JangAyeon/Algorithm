# day15: 과일 구매

import sys
input = sys.stdin.readline
from collections import deque
# 과일 갯수, 플레이어가 가진 돈
n,k=map(int, input().split())
f = []
# 과일의 가격 p, 포만감 c
for _ in range(n):
	price , c = map(int, input().split())
	#print(price,c, c//price)
	f.append([price, c, c//price])
# 포만감(내림), 조각포만감(내림), 가격(오름) 
f.sort(key=lambda x : (-x[2],-x[1]))
#print(f)

answer = 0
while True:
	price, c, pieceC = f[0]
	if k-price>=0:
		k-=price
		answer+=c
		f.pop(0)
		if k<=0 or not f:
			break
	elif k-1>=0:
		k-=1
		answer+=pieceC
		f[0]=[price-1,c,pieceC]
		if k<=0 or not f:
			break
		


print(answer)




