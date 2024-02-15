import sys
input = sys.stdin.readline

answer=[[1]*10]
n = int(input())

for i in range(1,n):
    temp = []
    for j in range(0, 10):
        #print(i,j, sum(answer[i-1][:j+1]))
        temp.append(sum(answer[i-1][:j+1]))
    answer.append(temp)
print(sum(answer[-1])% 10007)
