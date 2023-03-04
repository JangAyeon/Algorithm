import sys
input = sys.stdin.readline

n = int(input().strip())
ans = [1]*10

for i in range(n-1):
    for j in range(1,10):
       ans[j]+=ans[j-1]


    
print(sum(ans)%10007)