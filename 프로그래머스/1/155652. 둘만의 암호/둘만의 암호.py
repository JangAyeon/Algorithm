def solution(word, skip, index):
    answer = ''
    for w in word:
        turn =0
        s =  ord(w)
        while turn < index:
            s+=1
            if s>ord("z"):
                s=ord("a")
                
            if chr(s) not in skip:
                turn+=1
        ##print(turn, chr(s))
        answer+=chr(s)
    return answer