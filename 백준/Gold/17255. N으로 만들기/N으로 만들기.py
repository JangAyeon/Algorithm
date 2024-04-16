
import sys
input = sys.stdin.readline
N = input().strip()
n = len(N)
target = n*(n+1)//2
answers = set()

def dfs(left, right, result):
    if len(result)==target:
        answers.add(result)
        return
    if left>0:
        dfs(left-1, right, result+N[left-1:right+1])
    if right<n:
        dfs(left, right+1, result+N[left:right+2])
for i in range(n):
    dfs(i,i,N[i])
print(len(answers))