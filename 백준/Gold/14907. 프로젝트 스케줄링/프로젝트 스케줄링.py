import sys

able = [False]*26
arr = [[] for _ in range(26)]
cost = [0]*26
income = [0]*26
ans = [0]*26

for line in sys.stdin:
   info = line.split()
   num = ord(info[0][0]) - 65
   time = int(info[1])
   
   able[num] = True
   cost[num] = time
   
   if len(info) == 3:
       for next in map(lambda x: ord(x) - 65, info[2]):
           arr[num].append(next)
           income[next] += 1

q = []
for i in range(26):
   if income[i] == 0 and able[i]:
       ans[i] = cost[i]
       q.append((i, ans[i]))

idx = 0
result = 0
while idx < len(q):
   currNum = q[idx][0]
   currCost = q[idx][1]
   
   if not arr[currNum]:
       result = max(result, ans[currNum])
   
   for next in arr[currNum]:
       ans[next] = max(ans[next], currCost + cost[next])
       income[next] -= 1
       if income[next] == 0:
           q.append((next, ans[next]))
   idx += 1

print(result)
