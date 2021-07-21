#1
def plus_one(x):
    return x+1

print(plus_one(1))

#2
plus_two=lambda x: x+2
print(plus_two(1))

#3
a=[1,2,3]
print(list(map(plus_one,a)))

#4
a=[1,2,3]
print(list(map(lambda x:x+1, a)))