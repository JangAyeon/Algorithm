def zip_str(strings):
    min_length= 1001
    word = ""
    for s in strings:
        if min_length > len(s):
            #print(s, len(s))
            min_length = len(s)
            word = s
    return min_length, word

def solution(s):
    answer = []
    for i in range(1,(len(s)+1)//2+1):
        temp = []
        count = 1
        data = ""
        for j in range(0, len(s), i):
            #print(i, j, s[j:j+i], count)
            string = s[j:j+i]
            if temp:
                if temp[-1]!=string:
                    if count==1:
                        data +=temp.pop()
                    else:
                        data+=(str(count)+temp.pop())
                    count=1
                    temp.append(string)
                else:
                    count+=1
            else:
                temp.append(string)
        if temp:
            if count==1:
                data +=temp.pop()
            else:
                data+=(str(count)+temp.pop())
        answer.append(data)
        
    length, word = zip_str(answer)
    return length
    
