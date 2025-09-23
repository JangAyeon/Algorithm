import sys
input = sys.stdin.readline

n,m = map(int, input().split())
greater = [[] for _ in range(n+1)]
lighter = [[] for _ in range(n+1)]


for _ in range(m):
    heavy,light = map(int, input().split())
    greater[light].append(heavy)
    lighter[heavy].append(light)


def dfs(start,arr):
    global visited
    global check
    visited[start] = True
    for next_ in arr[start]:
        if not(visited[next_]):
            check+=1
            dfs(next_, arr)
    

        
mid =  (n + 1) / 2
answer=0
for start in range(1, n+1):
    visited = [False]*(n+1)
    check=0
    dfs(start,greater)
    if check>=mid:
        answer +=1

    check=0
    dfs(start,lighter)
    if check>=mid:
        answer +=1

print(answer)
"""
5 4
2 1
2 1
2 1
2 1
ans:0
"""