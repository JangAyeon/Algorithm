import sys
input=sys.stdin.readline


arr = list(map(str, input().strip()))
stack = []
answer = ""


for i in arr:
    if i.isalpha(): # A ~ Z 일 경우 바로 출력
        answer+=i
    elif i=="(": # stack에 추가
        stack.append(i)
    # 연산자 (*, /, +, - ) 우선 순위 고려 필요

    # stack 가장 위 연산자가 현재 연산자 우선 순위보다 높거나 동일한 경우
    # 내보내기
    elif i=="*" or i=="/":
        # *와 / 와 우선 순위가 동일하거나 높거나 연산자 : *과 / 뿐
        while stack and (stack[-1]=="*" or stack[-1]=="/"):
            answer+=stack.pop()
        stack.append(i)
    elif i=="+" or i=="-":
        # + 와 - 와 우선 순위가 동일하거나 높은 연산자 : +, -, *, /로 연산자 모두
        while stack and stack[-1] !="(": # 모두 내보내기
            answer+=stack.pop()
        stack.append(i)
    
    # 닫는 괄호 ( 는 여는 괄호 )가 나올 때까지 출력 
    elif i==")":
        while stack and stack[-1]!="(":
            answer+=stack.pop()
        stack.pop()


while stack:
    answer+=stack.pop()


print(answer)