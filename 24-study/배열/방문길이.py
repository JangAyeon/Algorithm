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


def solution(dirs):
    answer = set()
    que = deque()
    que.append([0,0])
    cmds = list(dirs)
    print(cmds)
    while que and cmds:
        cmd = cmds.pop(0)
        r,c = que.popleft()
        nr, nc = move(cmd, r,c)
        if not(-5<=nr<=5) or not(-5<=nc<=5):
            que.append([r,c])
            continue
        # print(cmd, r,c,nr, nc)
        que.append([nr, nc])
        answer.add((nr, nc, r, c))
        answer.add((r,c, nr, nc))
    #print(len(answer), que, cmds)
    return len(answer)//2