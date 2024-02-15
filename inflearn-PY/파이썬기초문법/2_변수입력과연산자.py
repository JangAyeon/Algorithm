#1
a=input("숫자를 입력하시오: ")
print(a)

#2
a,b=input("숫자를 입력하시오: ").split() 
#띄어쓰기로 분리되어 입력 (2, 3 입력)
print(a+b) 
#23 출력-> string 간의 + 연산

#3
a,b=map(int,input("숫자를 입력하세요: ").split())
#두 개 string 받고 split해서 int 형으로 변환
print(a+b) 
print(a-b)
print(a/b)
print(a*b)
print(a//b)
print(a%b)
print(a**b)

#4
#더 넓은 범위의 자료형으로 연산결과 출력됨
a=1 #정수 
b=4.3 #실수
print(a+b) #실수

