"""
1. 우선 24비트 버퍼에 위쪽(MSB)부터 한 byte씩 3 byte의 문자를 집어넣는다.
2. 버퍼의 위쪽부터 6비트씩 잘라 그 값을 읽고, 각각의 값을 아래 [표-1] 의 문자로 Encoding 한다
입력으로 Base64 Encoding 된 String 이 주어졌을 때, 
해당 String 을 Decoding 하여, 원문을 출력하는 프로그램을 작성하시오.    
"""

# 제시된 Decode 리스트
decode = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z',
  'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',
  '0','1','2','3','4','5','6','7','8','9','+','/'
  ]

T = int(input())
for idx in range(T):
    word = list(input()) # 입력 받은 문자열
    value = ""
    for j in range(len(word)):
        num = decode.index(word[j]) # 문자열의 각 문자를 숫자로 변환
        bin_num=str(bin(num)[2:]) # 이진수 변환시 앞에 붙은 0b 제거
        while len(bin_num)<6: # 앞에 0을 추가해 각 숫자들을 6자리 이진수로 표현
            bin_num="0"+bin_num
        value+=bin_num
    result = ""
    # 쭉 이어붙인 이진수들을 8자리씩 끊어서 십진수로 변환
    for j in range(len(value)//8):
        data = int(value[j*8:j*8+8],2)
        result+=chr(data) # 십진수를 아스키 코드로 변환
    print('#{0} {1}'.format(idx+1, result))