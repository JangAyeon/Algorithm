import sys
input = sys.stdin.readline

N = int(input().strip())

words = [input().strip() for _ in range(N)]

count=len(words)

for word in words:
    for j in range(1, len(word)):
        if word[j-1]!=word[j] and word[j] in word[:j]:
            #print(word[j-1],word[j], word[:j])
            count -=1
            break

print(count)