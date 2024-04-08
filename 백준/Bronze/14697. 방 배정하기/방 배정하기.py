a,b,c,student = map(int,input().split())
flag = 0
for i in range(student//a + 1):
	for j in range(student//b + 1):
		for k in range(student//c + 1):
			if a*i + b*j + c*k == student:
				flag = 1
				break

if flag == 1:
	print(1)
else:
	print(0)