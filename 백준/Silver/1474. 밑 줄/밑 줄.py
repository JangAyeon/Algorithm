import sys
input = sys.stdin.readline
from itertools import permutations

n,m =map(int, input().split())
words = [input().strip() for _ in range(n)]
length=0

for i in words:
    length+=len(i)
##print(words)
m-=length
j = len(words)-1
gap = m//j
plus = m%j
##print(length,m//j, m%j)

dashs= []
for _ in range(j):
    if plus>0:
        dashs.append(("_"*(gap+1)))
    else:
        dashs.append(("_"*(gap)))
    plus-=1

dashs = set(list(permutations(dashs)))

def create(dash, words):
    temp=[]
    for idx in range(len(dash)):
        temp.append(words[idx])
        temp.append(dash[idx])
    return "".join(temp+[words[-1]])
answers =[]
for dash in dashs:
    answers.append(create(dash, words))

answers.sort()
print(answers[0])