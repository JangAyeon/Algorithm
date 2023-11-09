# https://swexpertacademy.com/main/code/problem/problemDetail.do

T = int(input())
ans = []
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    arr = list(map(int, input().split()))
    avg=round(sum(arr)/len(arr))
    ans.append(avg)
    
for idx, value in enumerate(ans):
    print("#"+str(idx+1),value)
