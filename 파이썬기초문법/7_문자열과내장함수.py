#1
msg="It is Time"
print(msg.upper()) #대문자화
print(msg.lower()) #소문자화
print(msg) #원본 값을 그대로 유지됨

#2
msg="It is Time"
tmp=msg.upper()
print(tmp)

print(tmp.find("T")) 
#가장 앞에 있는 index 값 출력됨/없으면 -1

print(tmp.count("T"))
#T의 갯수

print(msg[:2])
#index 0번, 1번까지 슬라이싱해 출력

print(msg[3:5])
#index 3번, 4번까지 슬라이싱해 출력

print(len(msg))
#문자열 길이 출력

#3
for i in range(len(msg)): #index로 문자열 접근
    print(msg[i],end=" ")
print()

for x in msg: #for문으로 문자열 접근
    print(x, end=" ")
print()

#4
for x in msg:
    if x.isupper(): #대문자이면 출력
        print(x,end=" ")
print()

for x in msg:
    if x.islower(): #소문자이면 출력
        print(x,end=" ")
print()

for x in msg:
    if x.isalpha(): #띄어쓰기 없이 알파벳만 출력
        print(x, end=" ")
print()


#4
tmp="AZ"
for x in tmp:
    print(ord(x)) #아스키 넘버 출력

tmp="az"
for x in tmp:
    print(ord(x)) #아스키 넘버 출력

tmp=65
print(chr(tmp)) #아스키 넘버에 대응하는 문자 출력