import sys
input = sys.stdin.readline

graph = [list(map(str, input().split())) for _ in range(5)]
#print(graph)
answer = []

dr = [-1,1,0,0]
dc= [0,0,-1,1]

def dfs(row, col, word):
    if len(word)==6:
        if word not in answer:
            answer.append(word)

        return


    for idx in range(4):
        nr = row + dr[idx]
        nc = col + dc[idx]

        if not(0<=nr<5 and 0<=nc<5):
            continue
        dfs(nr, nc, word+graph[nr][nc])


for row in range(5):
    for col in range(5):
        dfs(row, col, graph[row][col])


print(len(answer))