from collections import deque

def move(cmd, r,c):
    if cmd=="L":
        return [r, c-1]
    if cmd =="R":
        return [r, c+1]
    if cmd=="U":
        return [r-1, c]
    if cmd=="D":
        return [r+1,c]
    
def isValidLoc(nr, nc):
    if not(-5<=nr<=5) or not(-5<=nc<=5):
        return False
    else:
        return True
    
def solution(dirs):
    answer = set()
    r,c=0,0
    for cmd in dirs:
        nr, nc = move(cmd, r, c)
        if not(isValidLoc(nr, nc)):
            continue
        answer.add((nr, nc, r, c))
        answer.add((r,c, nr, nc))
        r,c = nr,nc
    return len(answer)//2