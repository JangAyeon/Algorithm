import sys
input = sys.stdin.readline

n = int(input())
arr = input().strip()

answer = []
## R을 오른쪽으로
R_rlst = arr.rstrip("R")
answer.append(R_rlst.count("R"))

## B를 오른쪽으로
B_rlst=arr.rstrip("B")
answer.append(B_rlst.count("B"))
## R을 왼쪽으로
R_llst = arr.lstrip("R")
answer.append(R_llst.count("R"))

B_llst = arr.lstrip("B")
answer.append(B_llst.count("B"))

print(min(answer))