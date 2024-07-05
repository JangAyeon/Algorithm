## 최대한 많은 곡을 제대로 연주하려고 할 때
## 필요한 기타의 최소 개수
## 곡: 50개 이하
## 기타: 10개 이하

import sys
input = sys.stdin.readline
from itertools import combinations

n,m = map(int, input().split())
guitars=[]
plays = {}
result = [0 for _ in range(n+1)]
def change_yn(playlist):
    lst = []
    n = len(playlist)
    for idx in range(n):
        if playlist[idx]=="Y":
            lst.append(idx)
    return lst

def get_count(guitars):
    songs = []
    for g in guitars:
        songs+=plays[g]
    return len(set(songs))

for _ in range(n):
    a,b =  input().split()
    guitars.append(a)
    plays[a]=(change_yn(b))



for i in range(1,n+1):
    for temp in combinations(guitars, i):
        result[i] = max(result[i],get_count(temp))

max_song = max(result)
if max_song==0:
    print(-1)
else:

    print(result.index(max_song))


