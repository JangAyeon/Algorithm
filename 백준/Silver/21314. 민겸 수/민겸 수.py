import sys
input = sys.stdin.readline
from collections import Counter

arr = list(input().strip())
stack = []
min_=[]
max_=[]


def num(lst):
    count = Counter(lst)
    if lst[-1]=="K":
        max_.append((5*(10**count["M"])))
        if count["M"]:
            min_.append((10**(count["M"]-1)))

        min_.append((5))
    else:
        for _ in range(count["M"]):
            max_.append(1)
        min_.append((10**(count["M"]-1)))
    ##print(lst, min_,max_)



for i in arr:
    stack.append(i)
    if stack[-1]=="K":
        num(stack)
        stack = []

if stack:
    num(stack)
print("".join(list(map(str,max_))))
print("".join(list(map(str,min_))))
