# 문제 : https://www.acmicpc.net/problem/1316

import sys
input = sys.stdin.readline

n = int(input().strip())
words = [input().strip() for _ in range(n)]
res = n

for word in words:
    for i in range(0, len(word)-1):
        if word[i]==word[i+1]: 
        # 연속적으로 같은 글자 나온 경우
            pass
        elif word[i] in word[i+1:]:
        # 연속적으로 같은 글자가 나오지 않고 해당 글자가 뒤에 한 번 더 나오는 경우
            res-=1
            break
print(res)