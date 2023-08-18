import sys
input = sys.stdin.readline

n =  int(input().strip())
#print(n)
arr = sorted([list(map(int, input().split())) for _ in range(n)], key=lambda x : (x[1],x[0]))
res = []
'''
1. 회의가 빠르게 끝나면 더 많은 회의 가능
2. 회의가 끝나는 시간과 가까운 시작 시간
'''
previous_end_time = 0
for i in arr:
    start, end = i[0],i[1]
    if start>=previous_end_time:
        previous_end_time=end
        res.append(i)
print(len(res))