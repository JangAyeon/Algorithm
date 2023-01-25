import sys
input = sys.stdin.readline


n = int(input().strip())
arr=[[0,0,0]]
for _ in range(n):
    arr.append(list(map(int, input().split())))

ans = [[0,0,0] for _ in range(n+1)]


ans[1]=arr[1]
#print(n, arr,ans)

for i in range(2,n+1):
    ans[i][0]=min(ans[i-1][1], ans[i-1][2])+arr[i][0]
    ans[i][1]=min(ans[i-1][0], ans[i-1][2])+arr[i][1]
    ans[i][2]=min(ans[i-1][0], ans[i-1][1])+arr[i][2]

print(min(ans[-1]))