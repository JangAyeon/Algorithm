color_num,length=map(int,input().split())

color=[]
for i in range(color_num):
  color.append(int(input()))
  
dp = [0 for i in range(length+1)]
dp[0]=1

for j in color:
  for k in range(j,length+1):
      dp[k]+=dp[k-j]
      
print(dp[length])