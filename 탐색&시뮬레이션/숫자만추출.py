#code before lecture

string=input()
num="0123456789"
cnt=0
N=""
for x in string:
    if x in num:
        N+=x
N=int(N)

for i in range(1,N+1):
    if N%i==0:
        cnt+=1

print(N)
print(cnt)

