import sys
input = sys.stdin.readline
from collections import defaultdict

N,K = map(int,input().split())
data = [*map(int,input().split())]

sumlist = [0]
for i in range(N):
  sumlist.append(sumlist[-1]+data[i])


diffdict = defaultdict(int)
answer=0
for i in range(N+1):
  diff = sumlist[i]-K*i
  answer+=diffdict[diff]
  diffdict[diff]+=1



print(answer)