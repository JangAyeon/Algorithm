#1 빈 리스트 생성
import random as r
a=[]
b=list()

#2 리스트 생성
a=[1,2,3,4,5]
b=list(range(1,6))

#3 리스트 이어붙이기
c=a+b

#4 리스트 추가
a.append(6) #맨 마지막에 6 추가
a.insert(3,7) #3번 index에 7 추가

#5 리스트 꺼내기
a.pop() #가장 마지막 원소 꺼내기
a.pop(3) #3번 index 값 꺼내기
a.remove(4) #값 4 꺼내기

#6 index 번호 
a.index(5) #값 5의 index 번호

#7 리스트 총합/최대/최소
a=list(range(1,11))
sum(a) #a 리스트의 총합
max(a) #a 리스트의 최대값
min(a) #a 리스트의 최소값

#8 리스트 요소 무작위로 섞기
r.shuffle(a)

#9 리스트 정렬
a.sort(a) #오름차순
a.sort(reverse=True) #내림차순

#10 리스트 전체 삭제
a.clear() #빈 리스트

#11 리스트 슬라이싱
a=[23,12,36,53,19]
print(a[:3]) #[23,12,36]
print(a[1:4]) #[12,36,53]

#12 리스트 길이(값의 갯수)
print(len(a))

#13 리스트 값에 하나씩 접근
for i in range(len(a)):
    print(a[i],end=" ")
print()

for x in a:
    print(x, end=" ")
print()

for x in a:
    if x%2==1: #홀수만 출력
        print(x, end=" ")
print()

#14 enumerate : 리스트 값과 인덱스에 동시에 접근
for x in enumerate(a):
    print(x) #튜플 (index, value)

for x in enumerate(a):
    print(x[0], x[1]) 
    #튜플 형태 X, index와 value 차례로 출력됨

for index, value in enumerate(a):
    print(index, value)
    #튜플 형태 X, index와 value 차례로 출력됨

#15 리스트 vs 튜플
b=[1,2,3,4,5] # 값 변경 가능
print(b[0]) # 1 출력
b[0]=7
print(b[0]) # 7 출력

b=(1,2,3,4,5)
print(b[0]) # 1 출력
#b[0]=7 값 변경 불가능 -> 오류 발생
#print(b[0]) 

#16 all
if all (60>x for x in a): 
    #a의 모든 x가 60미만인 경우 참
    print("yes")
else:
    print("no")

#17 any
if any (15>x for x in a): 
    #a의 어떤 x가 15 미만인 경우 참
    print("yes")
else:
    print("no")

