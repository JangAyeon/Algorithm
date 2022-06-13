import sys
input=sys.stdin.readline
#https://velog.io/@minidoo/%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98-%EB%B6%84%ED%95%A0%EC%A0%95%EB%B3%B5-%EB%B0%B1%EC%A4%80-1629%EB%B2%88-%EA%B3%B1%EC%85%88

N,M,K=map(int, input().split())
#print(N,M,K)

print(pow(N,M,K))