import sys
input = sys.stdin.readline

n = int(input())


def fact(end):
    answer=1
    for i in range(1, end+1):
        answer*=i
    return answer

for _ in range(n):
    a,b = map(int, input().split())
    print(int(fact(b)/(fact(b-a)*fact(a))))
