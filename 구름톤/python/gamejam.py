# day 10: gamejam

import sys
input = sys.stdin.readline
from collections import deque

n = int(input())
# 1-indexing
groom = list(map(int, input().split()))
player = list(map(int, input().split()))
board = []
directions = []
for _ in range(n):
	board.append(input().split())
	


	
def move(r,c, step, direction,score, visited):
	
	while step!=0:
		#print(step,r,c,direction, score)
		if direction=="L":
			c = (c-1)%n
			r = r
		elif direction=="R":
			c = (c+1)%n
			r = r
		elif direction=="U":
			r = (r-1)%n
			c = c
		elif direction=="D":
			r = (r+1)%n
			c = c
		step-=1
		if visited[r][c]:
			return True, r, c, score
		else:
			visited[r][c]=True
			score+=1
		
	return False, r, c, score		
			


def game(r,c):
	visited = [[False]*(n) for _ in range(n)]
	que = deque()
	que.append([r,c])
	visited[r][c] = True
	score=1
	while que:
		r,c = que.popleft()
		step, direction = int(board[r][c][:-1]), board[r][c][-1]
		flag, nr, nc,score = move(r, c, step, direction, score, visited)
		if flag:
			return score
		else:
			que.append([nr,nc])

			

groomScore = game(groom[0]-1, groom[1]-1)
#print("goorm", groomScore)
#print("================")
playerScore = game(player[0]-1, player[1]-1)
#print("player", playerScore)

if groomScore>playerScore:
	print("goorm", groomScore)
else:
	print("player", playerScore)

	
