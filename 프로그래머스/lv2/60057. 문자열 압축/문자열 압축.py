def zip_s(count, chunk, result):
    
    if count == 1:
        result+=chunk
    else:
        result+=(str(count)+chunk)
    
    return result


def solution(s):
    
    answer = len(s)
    for unit in range(1, len(s)//2+1):
        chunk = s[0:unit]
        count = 1
        result = ""
        for start in range(unit, len(s), unit):
            #print("(unit, gap): ", unit, start)
            #print("chunk: ", chunk, ", slice: ", s[start:start+unit])
            #print("result: ", result)
            curr_chunk = s[start:start+unit]
            if chunk == curr_chunk:
                count+=1
            else:
                result = zip_s(count, chunk, result)
                chunk = curr_chunk
                count=1
        #print(unit,zip_s(count, chunk, result))
        answer = min(answer, len(zip_s(count, chunk, result)))
    return answer