#1 일차원 리스트 생성
a=[0]*5
print(a) #[0,0,0,0,0]

#2 이차원 리스트 생성
a=[[0]*3 for _ in range(3)]
print(a) #[[0, 0, 0], [0, 0, 0], [0, 0, 0]]
a[0][1]=1
a[2][0]=1
print(a)

#3 이차원 리스트 열 출력
for x in a:
    print(x)

for x in a:
    for y in x:
        print(y, end=" ")
    print()
