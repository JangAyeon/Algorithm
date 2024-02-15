#1
def add(a,b):
    print(a+b)
    return a+b

add(2,3)

#2
def add(a,b):
    c=a+b
    d=a-b
    return c,d #튜플 형태로 여러개 값 반환 가능

print(add(3,2))

#3
a=[12,13,7,9,19]

def isPrime(x):
    for i in range(2,x):
        if x%i==0:
            return False
    return True

for elem in a:
    if isPrime(elem):
        print(elem,end=" ")