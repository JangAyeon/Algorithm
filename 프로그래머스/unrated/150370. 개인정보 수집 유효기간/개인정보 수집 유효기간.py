def getPersonalDateTerm(info):
    date,term = info.split(" ")
    year,month,day = list(map(int, date.split(".")))
    return year, month, day,term

def createTermPeriod(terms):
    _terms = {}
    for term in terms:
        t, m = term.split()
        _terms[t] = int(m)
    return _terms

def createLastDate(period, yyyy,mm,dd):
    m = mm + period
    y = yyyy 
    d = dd
    if m>12:

        if m%12==0:
            y = y + (m//12)-1
            m = m%12
        else:
            y+=m//12
            m=m%12
        if m==0:
            m=12
    if d==0:
        d = 28
        m-=1
        if m==0:
            m=12
            
    #print(y,m,d)
    return  y, m,d

def checkDate(yyyy,mm,dd, today):
    y,m,d = list(map(int, today.split("."))) # 오늘
    
    # 보관이 불가능한 경우
    if yyyy<y:
        return False
    if (yyyy==y and mm<m):
        return False
    if (yyyy==y and mm==m and dd<=d):
        return False
    return True
    

def solution(today, terms, privacies):
    answer = []
    termPeriod = createTermPeriod(terms)
    #print(termPeriod)
    for idx, info in enumerate(privacies):
        yyyy, mm, dd, t = getPersonalDateTerm(info)
        _yyyy,_mm,_dd = createLastDate(termPeriod[t], yyyy,mm,dd)
        #print("last date", _yyyy,_mm,_dd)
        if not(checkDate(_yyyy,_mm,_dd, today)):
            answer.append(idx+1)


    return answer




