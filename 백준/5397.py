# 5397

import sys
input = sys.stdin.readline
from collections import deque 

n =int(input().strip())
arr = [input().strip() for _ in range(n)]

str_l = deque()
str_r = deque()

for word in arr:
    str_l = deque()
    str_r = deque()
    for letter in word:
        if letter == "<":
            if (str_l):
                str_r.append(str_l.pop())
        elif letter == ">":
            if (str_r):
                str_l.append(str_r.pop())
        elif letter =="-":
            if (str_l):
                str_l.pop()
        else:
            str_l.append(letter)
    ans = list(str_l) + list(reversed(str_r))
    print("".join(ans))