
"""
# 이퍼 - 문자열 압축
word = input()
n = len(word)
chunks = []
start = 0
ans = ""
for i in range(n-1):
	if word[i]!=word[i+1]:
		chunk=word[start:i+1]
		#print("chunck",chunk,i)
		start=i+1
		chunks.append(chunk)
chunks.append(word[start:]) # 마지막 청크 추가

for chunk in chunks:
	ans+=(chr(len(chunk)+64)) # 1개면 a
	if chunks[0][0]=="1":
		ans = "1"+ans

print(ans)
"""
"""
10101111
01111101
11001110
00000010
2
3 -1
1 1



import sys
input = sys.stdin.readline
from collections import deque

arr = [deque(map(int, input().strip())) for _ in range(4)]
m = int(input().strip())
cmd = []
for _ in range(m):
    a,b = map(int, input().split())
    cmd.append([a-1,b])
#print(arr, m, cmd)

def check_left(idx, direction):
    if idx<0 or arr[idx][2]==arr[idx+1][6]:
        return
    else:
        check_left(idx-1, -direction)
        arr[idx].rotate(direction)
    
def check_right(idx, direction):
    if idx>3 or arr[idx-1][2]==arr[idx][6]:
        return
    else:
        check_right(idx+1, -direction)
        arr[idx].rotate(direction)

def cal_score():
    res = 0
    for i in range(4):
        if arr[i][0]==1:
            res+=pow(2,i)
    return res
    
def solution():
    for idx, direction in cmd:
        check_left(idx-1, -direction)
        check_right(idx+1, - direction)
        arr[idx].rotate(direction)
    score = cal_score()
    return score

print(solution())
"""


"""
7
2 3 0
1 3 0
1 2 4 0
3 5 0
4 0
0
0
2
1 6
"""

import sys
input = sys.stdin.readline
from collections import deque

n = int(input())
graph = [0]
for _ in range(n):
    *a,b= map(int, input().split())
    graph.append(a)
m = int(input().strip())
start = list(map(int, input().split()))

visited = [0]*(n+1)
cnt = [0]*(n+1)
ans = [-1]*(n+1)
que = deque()

for i in start:
    que.append(i)
    ans[i]=0
    visited[i]=1
    
while que:
    curr =  que.popleft()
    for next in graph[curr]:
        if not visited[next]:
            #print("visitied",next)
            cnt[next]+=1
            if cnt[next]>=(len(graph[next])+1)//2:
                #print("counted")
                visited[next]=1
                ans[next]=ans[curr]+1
                que.append(next)
                
print(*ans[1:])