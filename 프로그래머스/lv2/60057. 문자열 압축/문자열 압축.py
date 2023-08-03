

def solution(s):
    
    # 가장 긴 길이인 문자열 전체 길이를 초기값으로 설정
    answer = len(s)
    
    # 문자열 슬라이스 길이가 절반을 넘어가면 압축 불가능함
    for unit in range(1, len(s)//2+1):
        zip_len = 0
        start = 0
        num = 1
        while start+unit <=len(s):
            sub = s[start:start+unit]
            while sub == s[start+unit*num: start+unit*(num+1)]:
                num+=1
            if num>1:
                zip_len+=len(str(num))
            zip_len+=len(sub)
            start+=unit*num
            num = 1
        zip_len +=len(s)-start
        answer = min(answer, zip_len)

    return answer

