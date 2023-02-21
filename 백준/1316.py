# 문제 : https://www.acmicpc.net/problem/1316

import sys
input = sys.stdin.readline

n = int(input().strip())
words = [input().strip() for _ in range(n)]
letters = [list(set(word)) for word in words]
#print(letters)
res = 0

for word in words:
    letter = list(set(word))
    visited=[False]*len(letter)
    prev = letter.index(word[0])
    cnt = 0
    for i in word:
        idx = letter.index(i)
        if not visited[idx]:
            visited[idx]=True
            cnt+=1
        else:
            if idx!=prev:
                #print("break")
                break
            else:
                cnt+=1
        #print("i",i ,"prev ",prev, "idx ",idx, "visited", visited)
        prev=idx
    if cnt==len(word):
        res+=1
        #print(word,res)
print(res)