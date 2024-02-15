#1 출력 결과 : [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
a=range(10)
print(list(a))

#2 출력 결과 : [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
a=range(1,11)
print(list(a))

#3
for i in range(10):
    print(i,"hello")

#4
for i in range(10,0,-1):
    print(i,"hello")

#5
i=1
while i<=10:
    print(i)
    i+=1

#6
i=10
while i>0:
    print(i)
    i-=1

#7
i=1
while True:
    print(i)
    if i==10:
        break
    i+=1

#8
for i in range(1,11):
    if i%2==0:
        continue
    print(i)

#9
for i in range(1,11):
    print(i)
    if i==5:
        break
else: #위의 if문에서 break 되어서 실행X
    print(11)

#10
for i in range(1,11):
    print(i)
    if i>20:
        break
else: #위의 if문 실행X여서 else문 실행O
    print(11)