#1. 1부터 N까지 홀수 출력하기

N=int(input("N을 입력하시오: "))
for i in range(1,N+1):
    if i%2==0:
        continue
    print(i)

#2. 1부터 N까지의 합 구하기
N=int(input("N을 입력하시오 : "))
total=0
for i in range(1,N+1):
    total+=i
print("총합 : ", total)

#3. N의 약수 출력하기
N=int(input("N을 입력하시오 : "))
for i in range(1,N+1):
    if N%i==0:
        print(i)