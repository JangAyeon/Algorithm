


arr = list(map(int,input()))
start = arr[0]
count = 1
answer = []
for idx in range(1, len(arr)):
	if start==arr[idx]:
		count+=1
		#print("같음", start, arr[idx])
	else:
		answer.append(chr(count+ord("A")-1))
		#print("다름", start, arr[idx],chr(count+ord("A")-1))
		start=arr[idx]
		count=1
answer.append(chr(count+ord("A")-1))		

if arr[0]==1:
	answer=[1]+answer
print("".join(answer))