
#1
x=7
if x==7:
    print("lucky")
    print("ㅋㅋㅋ")

#2
x=2
if x!=7:
    print("lucky")
    print("ㅋㅋㅋ")

#3
x=15
if x>=10:
    if x%2==1:
        print("10 이상의 홀수")

#4
x=7
if x>0 and x<10:
    print("x는 10보다 작은 자연수")

#5
x=7
if 0<x<10:
    print("x는 10보다 작은 자연수")

#6
x=10
if x>0:
    print("양수")
else:
    print("음수")


#7 출력 결과 : A
x=93
if x>=90:
    print("A")
elif x>=80:
    print("B")
elif x>=70:
    print("C")
elif x>=60:
    print("D")
else:
    print("E")

#8 출력 결과 : A B C D
x=93
if x>=90:
    print("A")
if x>=80:
    print("B")
if x>=70:
    print("C")
if x>=60:
    print("D")
