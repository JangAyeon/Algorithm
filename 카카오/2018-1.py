# 2018 KAKAO BLIND RECRUITMENT [1차] 비밀지도


def solution(n, arr1, arr2):
    answer = []
    for i, j in zip(arr1, arr2):
        j = bin(i|j)[2:] # 이진 연산
        line = j.zfill(n).replace("1","#").replace("0"," ") # 문자열 출력 형태 조절
        answer.append(line)
    return answer

#solution(5,[9, 20, 28, 18, 11],[30, 1, 21, 17, 28])