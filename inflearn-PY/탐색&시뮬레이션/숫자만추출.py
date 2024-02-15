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

#code from lecture
s=input()
res=0
for x in s:
    if x.isdecimal():
        res=res*10+int(x)
print(res)
cnt=0
for i in range(1,res+1):
    if res%i==0:
        cnt+=1
print(cnt)