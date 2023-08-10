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

def createDays(yyyy,mm,dd):
    days = yyyy*(28*12) + mm*28+dd
    return  days

def checkDate(keepsDays, today):
    if keepsDays<=today: # 보관 불가능
        return False
    else:
        return True
    

def solution(today, terms, privacies):
    answer = []
    termPeriod = createTermPeriod(terms)
    y,m,d = list(map(int, today.split("."))) # 오늘
    #print(termPeriod)
    for idx, info in enumerate(privacies):
        yyyy, mm, dd, t = getPersonalDateTerm(info)
        keepDays = createDays(yyyy,mm+termPeriod[t],dd)
        today = createDays(y,m,d)
        
        if not(checkDate(keepDays, today)):
            answer.append(idx+1)


    return answer



