#code before/after lecture
N=int(input())
arr=list(input().split())

def digit_sum(i):
    sum=0
    for x in i:
        sum+=int(x)
    return sum

max_num=0
max_sum=-2147000000
for i in arr:
    if max_sum<digit_sum(i):
        max_sum=digit_sum(i)
        max_num=int(i)
print(max_num)


#code from lecture (1) : 수식 이용
n=int(input())
a=list(map(int,input().split()))

def digit_sum(x):
    sum=0
    while x>0:
        sum+=x%10
        x=x//10
    return sum


max=-217000000
for x in a:
    total=digit_sum(x)
    if total>max:
        max=total
        res=x

#code from lecture (2) : iter과 형 변환 이용
n=int(input())
a=list(map(int,input().split()))

def digit_sum(x):
    sum=0
    for i in str(x): #한글자씩 받아서
        sum+=int(i) #숫자로 바꾸고 총합에 추가
    return sum


max=-217000000
for x in a:
    total=digit_sum(x)
    if total>max: #이전 총합보다 더 크면 갱신
        max=total
        res=x
